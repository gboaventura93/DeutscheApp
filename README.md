# DeutscheApp

I'm currently studying German and have tried many apps to learn the language. However, I’ve never found one that truly fit my style of learning while also being free. So, I decided to create my own app!

The first feature of *DeutscheApp* is a simple yet essential tool: guessing the articles of German nouns.

Articles are a critical part of mastering German. I’m currently at the B1 level and working towards B2 this year by taking various courses. While I’ve covered topics like Akkusativ, Dativ, and now Genitiv, I’ve realized that understanding articles is fundamental. Even if you know how to apply these grammatical cases, without the correct article, you cannot use them properly.

The app’s initial functionality focuses on guessing articles for A1-level words. In the future, I plan to expand its features by adding:
- New difficulty levels (Beginner, Intermediate, and Advanced).
- Additional learning tools and ideas as I continue studying and developing the app.

If you have any suggestions or ideas, I’d love to hear them! Feel free to share your thoughts or use the code as you wish.

## Get words to your app
Basically I ask ChatGPT for more words using this prompt:
```
I want a CSV file with 100 A1 German words, each with its article, separated into two columns: 'Article' and 'Word'.
Save the output as a CSV file I can download.
```
Then the CSV file will be available for download. Once downloaded, I copy and paste its contents into my main file. 

Since there’s a possibility that some entries might already exist in the main database, it’s important to remove duplicates. Typically, I handle this directly in Excel after paste the new content.
``` Data -> Data Tools -> Remove Duplicates ```

## When to use das, die or der? 🤔
There are several rules you can memorize to determine which article to use, but for me, it’s quite challenging to remember them all. It usually takes me a while to learn just one, so don’t rush to learn everything at once. Even learning one or two rules per week is a great achievement! 

Basically to identify the correct pronoun, you generally need to look at the suffix of the word. However, there are some general rules—and, of course, exceptions—that often contradict each other! 🤯

Regardless, here’s a list of some rules from [passion4teq](https://www.passion4teq.com/articles/der-die-das-gender-article-rules/) I found helpful, I strong recommend you to check it.

## Some Thoughts (German Tips)
I've already read somewhere that the neutral pronoun *das* appears far less frequently in German than *der* and *die*. Curious to confirm this, I checked a reliable source, [Duden.de](https://www.duden.de/sprachwissen/sprachratgeber/Die-Verteilung-der-Artikel-Genusangabe-im-Rechtschreibduden), which could confirm this affirmation:

<p align="center">
  <img src="https://raw.githubusercontent.com/gboaventura93/DeutscheApp/main/percentage.png" alt="Percentage Chart" width="350">
</p>


This shows that the feminine pronoun *die* is used in most cases (45.2%), followed by the masculine *der* (33.6%), and lastly the neutral *das* (21.2%).

Based on this, I’ve thought a simple personal strategy that I'd like to share:
If you’re unsure which pronoun to use, start with *die*, it gives you a 45.2% chance of being correct! If *die* sounds weird for you, try *der*. I only use *das* when I’m sure it’s the correct choice. 😊

