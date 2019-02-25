<h1> SHA128-Crack: </h1>

This program was created to break SHA128 hashes and return the original password. <br/>
This program uses a list of the 1,000,0000 most common passwords. <br/>
The original assignment required solving the problem using a brute force manner; However I decided to use a dictionary as an  optimization solution from the beginning.
  


<h3>Installation </h3>
 
* Clone or download the repository
* Profit!

<h3> Usage </h3>
Using the script is really easy. </br>

* Open the terminal or cmd
* Naviagate to where you cloned or downloaded the respositry.
* Type ```python python SHA128-Crack 'input the hash here' ``` (no need for quotes)
* Note: If you decide to use a salted hash, input the hash to break first then the salt word.
```python
python SHA128-Crack ece4bb07f2580ed8b39aa52b7f7f918e43033ea1 f0744d60dd500c92c0d37c16174cc58d3c4bdd8e
```

<h3> Solutions </h3>

The assignment asked break three different hashes:
  
* Easy Hash: b7a875fc1ea228b9061041b7cec4bd3c52ab3ce3
* Medium Hash: 801cdea58224c921c21fd2b183ff28ffa910ce31
* Hard Hash: ece4bb07f2580ed8b39aa52b7f7f918e43033ea1 w/salt hash: f0744d60dd500c92c0d37c16174cc58d3c4bdd8e



<h4> Notes </h3> 

_This code is far longer than it should be. I did not refactor the code. Methods should be created to keep from having repeated code_ 
