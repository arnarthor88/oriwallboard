import markdown

# Simple conversion in memory
""" md_text = '[id] Hello'
html = markdown.markdown(md_text)
print(html) """




import markdown

markdown.markdownFromFile(
    input='input.md',
    output='wallboard.html',
    encoding='utf8',
)