from collections import Counter

def word_count(text):
  return len(text.split())

def letter_count(text):
  letters = []
  
  for letter in list(text.lower()):
    if letter.isalpha():
      letters.append(letter)

  return dict(Counter(letters))

def report(text):
  str = '--- Begin report of books/frankenstein.txt ---\n'
  str += f'{word_count(text)} words found in the document\n\n'
  
  for letter, count in sorted(letter_count(text).items(), key=lambda x: x[1], reverse=True):
    str += f"The '{letter}' character was found {count} times\n"
  else:
    str += '--- End report ---'
  
  return str

def main():
  with open('books/frankenstein.txt', 'r') as f:
    file_contents = f.read()
    
    print(report(file_contents))

if __name__ == '__main__':
  main()