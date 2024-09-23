def search_quotes():
    while True:
        command = input("Enter command (name:author/tag:tag/tags:tag1,tag2/exit): ").strip()

        if command.startswith("name:"):
            author_name = command[len("name:"):].strip()
            author = Author.objects(fullname=author_name).first()
            if author:
                quotes = Quote.objects(author=author)
                for quote in quotes:
                    print(f"Quote: {quote.quote}")
            else:
                print(f"No quotes found for {author_name}")

        elif command.startswith("tag:"):
            tag = command[len("tag:"):].strip()
            quotes = Quote.objects(tags=tag)
            for quote in quotes:
                print(f"Quote: {quote.quote}")

        elif command.startswith("tags:"):
            tags = command[len("tags:"):].strip().split(',')
            quotes = Quote.objects(tags__in=tags)
            for quote in quotes:
                print(f"Quote: {quote.quote}")

        elif command == "exit":
            print("Exiting...")
            break

        else:
            print("Invalid command. Try again.")

# Start search
search_quotes()
