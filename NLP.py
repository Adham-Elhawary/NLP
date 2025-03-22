import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
###############################################################
nltk.download('vader_lexicon')
analyzer = SentimentIntensityAnalyzer()

#################################################################################################################################
def analyze_sentiment(text):
    scores = analyzer.polarity_scores(text)
    compound_score = scores['compound']
    sentiment_map = {
        compound_score >= 0.05: "Positive",
        compound_score <= -0.05: "Negative",
        True: "Neutral"
    }
    sentiment = next((v for k, v in sentiment_map.items() if k), "Neutral")
    return scores, sentiment
#################################################################################################################################
def display_results(text, scores, sentiment):
    print("\nSentiment Analysis Results:")
    print(f"Text: {text}")
    print(f"bad: {scores['neg']:.3f}")
    print(f"Neutral: {scores['neu']:.3f}")
    print(f"good: {scores['pos']:.3f}")
    print(f"Compound: {scores['compound']:.3f}")
    print(f"Sentiment: {sentiment}\n")
#################################################################################################################################
def main():
    text = input("Enter text to analyze: ").strip()
    if not text:
            print("Please enter some text!\n")
    try:
        scores, sentiment = analyze_sentiment(text)
        display_results(text, scores, sentiment)
    except Exception as e:
        print(f"An error occurred during sentiment analysis: {e}\n")
#################################################################################################################################
if __name__ == "__main__":
    main()
