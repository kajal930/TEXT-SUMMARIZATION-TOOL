from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

def summarize_text(text, sentence_count=3):
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document, sentence_count)
    return " ".join(str(sentence) for sentence in summary)

if __name__ == "__main__":
    print("------ TEXT SUMMARIZATION TOOL ------\n")
    input_text = input("Enter the article or paragraph:\n\n")
    try:
        num_sentences = int(input("\nHow many sentences should the summary contain? (e.g., 2, 3): "))
    except ValueError:
        num_sentences = 3
        print("Invalid input. Defaulting to 3 sentences.")
    
    summary_result = summarize_text(input_text, num_sentences)
    
    print("\n------ SUMMARY ------")
    print(summary_result)
