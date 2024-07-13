from django.shortcuts import render
from django.utils.html import format_html

def highlight_words(request, words):
    words_list = words.split(',')
    word_with_most_unique_letters = max(words_list, key=lambda word: len(set(word)))

    highlighted_words = [
        format_html('<span style="background-color: yellow;">{}</span>', word)
        if word == word_with_most_unique_letters else word
        for word in words_list
    ]

    output = ', '.join(highlighted_words)
    return render(request, 'index.html', {'output': output})
