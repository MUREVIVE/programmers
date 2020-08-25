- modified content, untracked content 문제로 1시간 넘게 헤맨 것을 해결

https://secjong.tistory.com/2

<br>

- git status할 시 한글 깨짐 현상 발생 (ex : 123/45/335...)

: git config --global core.quotepath false

<br>

- programmers 폴더를 push한 후 git에 여전히 programmers/sql/...sql 와 같이 untracked file이 존재하는 경우

: git clean -f 를 사용하여 해결. (더 자세한건 구글에 쳐볼 것.)

<br>

- github에 repository 새로 만들고자 할 때 (원하는 폴더만 저장하는게 아니라 자꾸 git내 전체 폴더들이 저장돼서 적는다.)

: github에 repository를 만든 후, local repository에서 해당 repository의 이름을 가진 폴더가 git폴더에 있어야 한다.

(예를 들어 programmers 폴더라고 하면, 이 폴더는 empty 상태여서는 안된다.)

: 처음으로 push하고자 하는 파일이 programmers/sql/asdf.sql이라고 한다면, git bash에서 경로가 ~/git/programmers에 와서

: git init / git add sql / git commit ~ / git remote ~ / git push -u origin master 

: 위 과정을 거치는 것임.
