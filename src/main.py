from texts.text_generator import TextGenerator

if __name__ == '__main__':
    text_generator = TextGenerator('./datasets/quotes.csv')

    for _ in range(10):
        print(text_generator.random_text('genre', 'authoar'))
