# Cistercian Numbers with Numpy

This project is inspired by the following tweet:

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">The Cistercian monks invented a numbering system in the 13th century which meant that any number from 1 to 9999 could be written using a single symbol <a href="https://t.co/VRuEx4dkPF">pic.twitter.com/VRuEx4dkPF</a></p>&mdash; UCL Department of Mathematics (@MathematicsUCL) <a href="https://twitter.com/MathematicsUCL/status/1356558846093914114?ref_src=twsrc%5Etfw">February 2, 2021</a></blockquote> 

![Image of Cistercian symbols](https://github.com/anatshk/cistercian_numbers/blob/main/cistercian_symbols.jpeg)

I'd like to use Numpy 2D arrays to represent the Cistercian number symbols and create a function that translates Arabic numerals to Cistercian symbols and back.

Then, I'd like to try and train a small CNN to see if it can decipher the Cistercian number symbols.

---

***2021-02-05 Update***: run `show_cistercian_number.py` for an interactive CLI converting Arabic Numerals to Cistercian number symbols.
Be prepared for unhandled exceptions for non-integers, or numbers outside of the [1-9999] range.
Close figures to continue interacting with CLI.
