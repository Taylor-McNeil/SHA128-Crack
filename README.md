<h1> SHA128-Crack: </h1>
Author: Taylor McNeil

This program was created to break SHA128 hashes and return the original password. <br/>
This program uses a list of the 1,000,0000 most common passwords. <br/>
The original assignment required solving the problem using a brute force manner; However I decided to use a dictionary as an  optimization solution from the beginning.</br>
!!Note: I wrote only wrote an optimized solution. I did not start with brute force loops.  


<h3>Installation </h3>
 
* Clone or download the repository
* Profit!

<h3> Usage </h3>
Using the script is really easy. </br>

* Open the terminal or cmd
* Navigate to where you cloned or downloaded the repository.
* Type ```python SHA128-Crack input the hash here ``` 
* Note: If you decide to use a salted hash, input the hash to break first then the salt word.
```python
python SHA128-Crack ece4bb07f2580ed8b39aa52b7f7f918e43033ea1 f0744d60dd500c92c0d37c16174cc58d3c4bdd8e
```
* The output will be the password if found, the total attempts and the total time since the start of the program

<h3> Solutions </h3>

The assignment was to break three different hashes:
  
* Easy Hash: b7a875fc1ea228b9061041b7cec4bd3c52ab3ce3
* Medium Hash: 801cdea58224c921c21fd2b183ff28ffa910ce31
* Hard Hash: ece4bb07f2580ed8b39aa52b7f7f918e43033ea1 w/salt hash: f0744d60dd500c92c0d37c16174cc58d3c4bdd8e

The Solutions are as follows:
* Easy Password: letmein
* Medium Password: vjhtrhsvdctcegth
* Hard Password: slayerharib salt word: slayer 


<h4> Notes </h3> 

_This code is far longer than it should be. I did not refactor the code. Methods should be created to keep from having repeated code. As of 2/24/2019 there is not any handling for if the user inputs the incorrect arguments._ 
