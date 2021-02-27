# git1_CDV


### About project in CDV for GIT TRAINING

### Here is new Python image:
![alt text](https://applover.pl/wp-content/uploads/2020/01/kisspng-python-computer-icons-programming-language-executa-5d0f0aa7c78fb3.0414836115612668558174-1024x1024.png "Python logo")


[link to GIT tutorial](https://www.udemy.com/course/git-od-podstaw-dla-kazdego/)


## movies about Appium 
[![link to video](![image](https://user-images.githubusercontent.com/79729260/109389128-599d1500-790b-11eb-915d-0732b297a1a4.png)
)](https://www.youtube.com/watch?v=UlktcBntD6sYOUTUBE_VIDEO_ID_HERE)


----
**Test Schedule**
----
- [ ] Test new features
- [x] Retests
- [ ] Regression


## Useful links
[How to use markdown](https://guides.github.com/features/mastering-markdown/)

:+1: :octocat:

[Link to GIT tutorial](https://www.udemy.com/course/git-od-podstaw-dla-kazdego/)

### Sample code Python+Selenium Webdriver 
import unittest
from selenium import webdriver
```Python
class BaseTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://wizzair.com/pl-pl#/")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()
 ```       

### Links 
  

### Picture  


### Fav git commands

Git setup | Git configuration
------------ | -------------
git init [directory] | git config --global user.name "[your_name]"
git clone [repo / URL] | git config --global user.email "[email_address]"
git clone [repo / URL] [folder] | git config --global color.ui auto

### Fav terminal commands 

#### Manual post-release actions

The job will also create a Merge Request of this tag back to `develop` branch.
This MR is just a reminder – it is always impossible to merge it from GUI because there are conflicts.

Make sure you have maintainer role to the repo (required to directly push to `develop` branch) and execute:
```
git pull
git checkout develop
git merge <tag>
<manually resolve conflicts on CHANGELOG.md>
git commit
git push
```

Then close the MR without merging.

### Hotfix

Hotfix = bug is on production but you don't want to release develop.
As result the fix will be deployed from the last existing release branch.

We have a policy to create MR to both release branch and `develop` to see problems on `develop` faster (E2E tests run only on `develop`).

1. Create a branch from release branch: `git checkout -b yourbranch release-x.y`
1. Commit fixes to your branch
1. Create a branch from develop and cherry-pick your fixes: `git checkout -b yourbranch-dev develop && git cherry-pick yourbranch`
1. `git push -u origin yourbranch yourbranch-dev`
1. Create a Merge Request of _yourbranch_ to the old release branch
1. Create a Merge Request of _yourbranch-dev_ to `develop`
1. Accept MRs to the release branch and `develop`
1. Test on stage
1. Run release (see above) on release branch


Code sample:
```python
if __name__ == "__main__":
    # ...to uruchamiam testy
    unittest.main(verbosity=2)
```
