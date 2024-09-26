# Extractive summary
from transformers import pipeline

def extract_summary(input_text):
    summarizer = pipeline("summarization")
    summary = summarizer(input_text, max_length=500, min_length=10)
    return summary


# Abstractive summary
from transformers import T5Tokenizer, T5ForConditionalGeneration, pipeline

def abstract_summary(input_text):
    checkpoint = "MBZUAI/LaMini-Flan-T5-248M"
    tokenizer = T5Tokenizer.from_pretrained(checkpoint)
    base_model = T5ForConditionalGeneration.from_pretrained(checkpoint)

    pipe_sum = pipeline(
        'summarization',
        model=base_model,
        tokenizer=tokenizer,
        max_length=500,
        min_length=10
    )
    summary = pipe_sum(input_text)
    return summary

# input_text = "Out of another, I get a lovely view of the bay and a little private wharf belonging to the estate. There is a beautiful shaded lane that runs down there from the house. I always fancy I see people walking in these numerous paths and arbors, but John has cautioned me not to give way to fancy in the least. He says that with my imaginative power and habit of story-making a nervous weakness like mine is sure to lead to all manner of excited fancies and that I ought to use my will and good sense to check the tendency."

# print("______________________________________________________________________________________")
# print(extract_summary(input_text))
# print("______________________________________________________________________________________")
# print(abstract_summary(input_text))