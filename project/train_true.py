import torch
from datasets import load_dataset
from torch.utils.data import DataLoader
from transformers import GPT2Tokenizer, GPT2LMHeadModel
from tqdm import tqdm
from functools import partial
from torch.optim import AdamW
import os

os.environ["HSA_OVERRIDE_GFX_VERSION"] = "10.3.0"
os.environ["HIP_VISIBLE_DEVICES"] = "0"
os.environ["ROCM_ENABLE_PRE_VEGA"] = "1"


def tokenize_function(examples, tokenizer):
    questions = [q[0] if isinstance(q, tuple) else q for q in examples['question']]
    answers = examples['answer']       #1

    texts = [f"Question: {q} Answer: {a}" for q, a in zip(questions, answers)] #2

    tokenized = tokenizer(
        texts,
        truncation=True,
        padding='max_length',
        max_length=192,
        return_tensors="pt"
    )              #3
    tokenized["labels"] = tokenized["input_ids"].clone()
    return tokenized


if __name__ == "__main__":
    device = torch.device("cuda")#1

    tokenizer = GPT2Tokenizer.from_pretrained("model_gpt-2.2")
    model = GPT2LMHeadModel.from_pretrained("model_gpt-2.2").to(device)#2

    dataset = load_dataset("its5Q/yandex-q", trust_remote_code=True)
    train_dataset = dataset['train']#3




    tokenize_fn = partial(tokenize_function, tokenizer=tokenizer) #1
    train_dataset = train_dataset.map(
        tokenize_fn,
        batched=True,
        batch_size=1000,
        num_proc=4,
        remove_columns=train_dataset.column_names
    )#2
    train_dataset.set_format(type="torch", columns=["input_ids", "attention_mask", "labels"])#3


    train_dataloader = DataLoader(
        train_dataset,
        batch_size=16,
        shuffle=True,
        num_workers=4,
        pin_memory=True
    )#1

    optimizer = AdamW(model.parameters(), lr=2e-5)#2

    for epoch in range(1):#3
        model.train()
        total_loss = 0
        progress_bar = tqdm(train_dataloader, desc=f"Epoch {epoch + 1}/5")

        for batch in progress_bar:
            inputs = {
                "input_ids": batch["input_ids"].to(device),
                "attention_mask": batch["attention_mask"].to(device),
                "labels": batch["labels"].to(device)
            }

            optimizer.zero_grad()
            outputs = model(**inputs)
            loss = outputs.loss
            loss.backward()
            optimizer.step()

            total_loss += loss.item()
            progress_bar.set_postfix({"loss": loss.item()})
        model.save_pretrained("model_gpt-2.3")
        tokenizer.save_pretrained("model_gpt-2.3")

        print(f"Epoch {epoch + 1} Avg Loss: {total_loss / len(train_dataloader):.4f}")

        # Тест генерации
        model.eval()
        input_text = "Question: что такое нейросеть? Answer:"
        inputs = tokenizer(input_text, return_tensors="pt").to(device)
        outputs = model.generate(
            inputs.input_ids,
            max_length=100,
            do_sample=True,
            top_p=0.9,
            temperature=0.7,
            pad_token_id=tokenizer.eos_token_id
        )
        print(tokenizer.decode(outputs[0], skip_special_tokens=True))