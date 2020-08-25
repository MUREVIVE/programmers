

## command 정리 모음

- **git init** : 현재 디렉토리를 Git이 관리하는 프로젝트 디렉토리(=working directory)로 설정하고 그 안에 레포지토리(.git 디렉토리) 생성

- **git reset [파일 이름]** : staging area에 올렸던 파일 다시 내리기

- **(git reset *)** : staging area에 올렸던 모든 파일 다시 내리기

- **git add .** : working directory 내의 수정사항이 있는 모든 파일들을 staging area에 올리기

(git add *와 동일)

- **git push** : local repository의 내용 -> remote repository에 반영

    1. 원칙적으로 자신의 리모트 레포지토리에는 자신만 git push를 할 수 있습니다. 

    2. 만약 다른 사용자도 git push를 할 수 있게 해주려면 그 사용자를 해당 리모트 레포지토리의 collaborator로 지정하면 됩니다. 

<br> <br>

- **git pull** : remote repositry 내용 -> local repository에 반영

    1. remote repository의 최신 내용이 더 앞서있는 경우

    2. 다른 사람이 remote repository에 자신의 컴퓨터로 가져가서 수정한 다음 git push한 경우 나는 git pull을 사용해야함.

- **cat 파일이름** : 해당 파일 내용 출력

- **git push --set-upstream origin master** : local repository의 내용을 처음으로 GitHub의 remote repository로 보낼 때

- **git clone git주소** : github 프로젝트의 repository를 그대로 복제.

    (주로 처음 가지고 올 때 사용.)

- **git push -u origin master** : local repository의 내용을 처음으로 remote repository에 올릴 때 사용.

<br> <br>

- **git log** : commit history 확인

- **git log --pretty=oneline** : commit history를 좀 더 예쁘게 확인

- **git show** : 어떤 파일이 어떻게 변했는지 확인 가능

- **git commit에서 -m을 붙이지 않았을 경우** : text editor에 commit message를 남기면 된다. (주로 복잡하고 긴 commit message인 경우 사용.)

- **git commit --amend** : 최신 commit 수정하여 새로운 commit으로 만들기

- **git config alias.[새로운 별명] [길이가 긴 커맨드]** : 길이가 긴 커맨드를 짧은 별명만 타이핑해도 실행 가능.

<br> <br>

- **cat 파일** : 해당 파일 내용 출력

- **HEAD** : 어떤 commit 하나를 가리킴. HEAD가 가리키는 commit에 따라

working directory 구성

<br> <br>

