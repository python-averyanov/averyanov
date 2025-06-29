from transformers import GPT2LMHeadModel, GPT2Tokenizer
device = 'cpu'
model = GPT2LMHeadModel.from_pretrained("model_gpt-2.4")
tokenizer = GPT2Tokenizer.from_pretrained("model_gpt-2.4")
def generate_answer(question):
    model.eval()
    inputs = tokenizer(question, return_tensors="pt").to(device)
    outputs = model.generate(
        inputs.input_ids,
        max_length=200,
        do_sample=True,
        top_p=0.90,
        temperature=0.35,
        pad_token_id=tokenizer.eos_token_id,
        no_repeat_ngram_size=3,
    )
    ara = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return ara
# input_text = input('введите запрос: ')
# generate_answer(input_text)
