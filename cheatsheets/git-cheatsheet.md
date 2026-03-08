# Git 명령어 모음

---

## 1. 설정 (Configuration)

`git config` : Git 환경 설정 조회 및 변경

- `git config --global user.name "이름"` : 전역 사용자 이름 설정 (모든 저장소에 적용)
- `git config --global user.email "이메일"` : 전역 사용자 이메일 설정
- `git config --list` : 현재 적용된 모든 설정값 확인 (이름, 이메일, 에디터 등)
- `git config user.name` : 현재 설정된 이름만 출력 (로컬 설정이 있으면 로컬 우선)
- `git config --global core.editor "code --wait"` : 기본 에디터를 VS Code로 변경 (`--wait`가 없으면 Git이 에디터 종료를 기다리지 않음)
- `git config --global alias.[단축어] [명령어]` : 긴 명령어를 단축어로 등록 (예: `git config --global alias.co checkout` → `git co`로 사용 가능)

---

## 2. 시작하기 (Setup)

`git init` : 현재 디렉토리를 Git 저장소로 초기화 (`.git` 폴더 생성, 이미 있는 폴더에서도 사용 가능)

`git clone [URL]` : 원격 저장소 전체를 내 컴퓨터로 복제

> 내부적으로 `mkdir` -> `git init` -> `git remote add` -> `git fetch` + `git checkout` 순으로 동작
- `git clone [URL] .` : 현재 폴더(반드시 빈 폴더)에 하위 폴더 없이 파일을 바로 받아옴 (폴더명 중복 방지에 유용)
- `git clone -b [브랜치명] [URL]` : 특정 브랜치만 골라서 클론 (기본값은 `main` 또는 `master`)
- `git clone --depth 1 [URL]` : 최신 커밋 1개만 받아오는 얕은 클론 (대형 저장소를 빠르게 받을 때 유용)

---

## 3. 상태 확인 및 변경사항 감지 (Inspect)

`git status` : 작업 디렉토리의 파일 상태 확인 (수정됨 / 스테이징됨 / 추적 안 됨 등)
- `git status -s` : 파일 상태를 짧게 요약 출력 (Short 모드, `M`=수정, `A`=추가, `??`=미추적)

`git diff` : 파일의 구체적인 변경 내용(코드) 비교
- `git diff` : `git add` 전, 작업 디렉토리와 최근 커밋 간의 차이 확인
- `git diff --staged` : `git add` 후, 커밋 예정인 파일들의 변경 내용 확인 (`--cached`와 동일)
- `git diff [브랜치A] [브랜치B]` : 두 브랜치 간의 전체 코드 차이 비교
- `git diff --name-only` : 변경된 파일 이름 목록만 출력 (코드 내용 제외)
- `git diff [커밋해시A] [커밋해시B]` : 두 커밋 사이의 차이 비교

`git blame [파일명]` : 파일의 각 줄을 누가, 언제, 어떤 커밋으로 수정했는지 표시 (버그 유발자 추적에 유용)

---

## 4. 스테이징 및 커밋 (Snapshot)

`git add` : 파일을 스테이징 영역(장바구니)에 추가

- `git add .` : 현재 디렉토리 기준으로 변경된 모든 파일(삭제 포함) 스테이징
- `git add [파일명]` : 특정 파일만 선택해서 스테이징
- `git add -p` : 파일을 통째로 올리지 않고, 변경된 코드 덩어리(Hunk)별로 보면서 선택적으로 스테이징 (정밀한 커밋 분리에 유용)

`git commit` : 스테이징된 변경 사항을 확정하여 히스토리에 기록

- `git commit -m "메시지"` : 에디터를 열지 않고 커밋 메시지를 인라인으로 작성
- `git commit -am "메시지"` : `git add` + `git commit`을 한 번에 처리 (단, 새로 생성된 파일은 포함 안 됨)
- `git commit --amend` : 가장 최신 커밋을 수정 (빠뜨린 파일 추가 또는 메시지 수정, 이미 푸시한 커밋엔 주의)
- `git commit --amend -m "새 메시지"` : 최신 커밋 메시지만 즉시 덮어쓰기
- `git commit --amend --no-edit` : 커밋 메시지는 유지하고 파일 내용만 수정

---

## 5. 히스토리 조회 (Log)

`git log` : 전체 커밋 히스토리를 시간 역순으로 조회

- `git log -n` : 최근 n개의 커밋만 보기 (예: `git log -3`)
- `git log -p` : 각 커밋의 변경된 코드 내용(diff)까지 상세 표시
- `git log --oneline` : 커밋 해시(앞 7자리)와 제목만 한 줄로 요약
- `git log --graph` : 브랜치 분기·병합 흐름을 ASCII 그래프로 시각화
- `git log --oneline --graph --all` : 모든 브랜치의 흐름을 한눈에 확인 (가장 추천하는 조합)
- `git log -- [파일명]` : 특정 파일의 변경 이력만 필터링
- `git log --follow [파일명]` : 파일 이름이 중간에 바뀌었어도 이전 기록까지 추적
- `git log --author="이름"` : 특정 작성자의 커밋만 검색
- `git log --grep="키워드"` : 커밋 메시지에 특정 단어가 포함된 커밋 검색
- `git log --since="2024-01-01" --until="2024-12-31"` : 특정 기간의 커밋만 조회

`git reflog` : `HEAD`가 이동한 모든 기록 조회 (실수로 지운 커밋·브랜치 복구 시 필수, 기본 90일 보관)

---

## 6. 브랜치 관리 (Branching)

`git branch` : 로컬 브랜치 목록 조회 (현재 브랜치는 `*` 표시)

- `git branch -r` : 원격(Remote) 브랜치 목록 조회
- `git branch -a` : 로컬과 원격의 모든 브랜치 조회
- `git branch -vv` : 로컬 브랜치가 어떤 원격 브랜치와 연결(추적)되어 있는지 확인
- `git branch [브랜치명]` : 새 브랜치 생성 (이동은 하지 않음)
- `git branch -m [새이름]` : 현재 브랜치 이름 변경
- `git branch -d [브랜치명]` : 병합이 완료된 브랜치 삭제 (미병합 시 오류 발생)
- `git branch -D [브랜치명]` : 병합 여부와 상관없이 강제 삭제

`git switch` : 브랜치 이동 (`git checkout`의 이동 기능에서 분리된 명령어, Git 2.23+)

- `git switch [브랜치명]` : 해당 브랜치로 이동
- `git switch -c [새브랜치]` : 새 브랜치를 생성하고 즉시 이동 (`git checkout -b`와 동일)
- `git switch -` : 바로 직전에 있었던 브랜치로 이동

---

## 7. 병합 및 동기화 (Merge & Rebase)

`git merge` : 다른 브랜치의 내용을 현재 브랜치로 합침

- `git merge [대상브랜치]` : 대상 브랜치를 현재 브랜치에 병합 (Fast-forward 가능하면 자동 적용)
- `git merge --no-ff [대상브랜치]` : Fast-forward가 가능해도 강제로 병합 커밋을 남김 (히스토리 보존, 팀 협업 시 권장)
- `git merge --squash [대상브랜치]` : 대상 브랜치의 모든 커밋을 하나로 합쳐 스테이징 (커밋은 직접 해야 함)
- `git merge --abort` : 병합 중 충돌(Conflict) 발생 시 병합 취소 후 되돌림

`git rebase` : 브랜치의 베이스(시작점)를 재설정하여 히스토리를 일직선으로 만듦

- `git rebase [대상브랜치]` : 내 브랜치의 변경 사항을 대상 브랜치의 최신 커밋 뒤로 이어 붙임
- `git rebase -i HEAD~[숫자]` : 최근 커밋 n개를 대화형으로 편집 (합치기·메시지수정·순서변경 등 가능)
- `git rebase --abort` : 리베이스 진행 중 취소하고 원래 상태로 복구
- `git rebase --continue` : 충돌 해결 후 리베이스 재개

`git cherry-pick [커밋해시]` : 다른 브랜치의 특정 커밋 하나만 복사해서 현재 브랜치로 가져옴 (핫픽스 적용 시 유용)

---

## 8. 원격 저장소 제어 (Remote)

`git remote` : 원격 저장소 연결 관리

- `git remote -v` : 연결된 원격 저장소의 주소(URL) 확인 (fetch/push 구분하여 표시)
- `git remote add origin [URL]` : 원격 저장소 주소 추가 (`origin`은 관례적 이름)
- `git remote remove origin` : 기존 원격 저장소 연결 삭제
- `git remote set-url origin [새URL]` : 원격 저장소 주소 변경
  - GCM → SSH: `git remote set-url origin git@github.com:아이디/프로젝트명.git`
  - SSH → GCM: `git remote set-url origin https://github.com/아이디/프로젝트명.git`

`git push` : 로컬의 변경 사항을 원격 저장소로 업로드

- `git push -u origin [브랜치명]` : 업스트림(추적 브랜치)을 설정하며 푸시 (최초 1회 필수, 이후엔 `git push`만 입력해도 됨)
- `git push origin [브랜치명]` : 지정한 브랜치 푸시
- `git push --all` : 로컬의 모든 브랜치를 원격으로 푸시
- `git push --force` / `-f` : 원격 내용을 무시하고 강제 덮어쓰기 (협업 시 매우 위험)
- `git push --force-with-lease` : 다른 사람이 새로 푸시한 내용이 없을 때만 강제 푸시 허용 (`--force`보다 안전)
- `git push origin --delete [브랜치명]` : 원격 저장소의 브랜치 삭제

`git fetch` : 원격 저장소의 최신 이력을 가져오기만 함 (로컬 작업 내용에 영향 없음)

- `git fetch --prune` : 원격에서 이미 삭제된 브랜치를 로컬 원격 추적 목록에서도 정리

`git pull` : 원격의 내용을 가져와서 현재 브랜치에 합침 (`git fetch` + `git merge`)

- `git pull origin [브랜치명]` : 원격 브랜치를 가져와 병합
- `git pull --rebase` : 병합 대신 리베이스 방식으로 적용 (병합 커밋 없이 로그가 깔끔해짐)

---

## 9. 되돌리기 및 복구 (Undo)

`git restore` : 파일의 변경 사항 취소 (`git checkout`의 복구 기능에서 분리, Git 2.23+)

- `git restore [파일]` : 파일의 수정 내용을 취소하고 마지막 커밋 상태로 되돌림 (복구 불가)
- `git restore --staged [파일]` : 스테이징된 파일을 내림 (Unstage, 파일 내용은 유지)

`git reset` : 커밋을 취소하고 과거 시점으로 HEAD를 이동 (히스토리가 삭제됨, 푸시 후엔 주의)

- `git reset --soft HEAD~1` : 최신 커밋 취소, 변경 내용은 스테이징 상태로 보존 (커밋만 다시 하고 싶을 때)
- `git reset --mixed HEAD~1` : 기본값. 커밋 취소 + 스테이징 해제, 작업 내용은 유지
- `git reset --hard HEAD~1` : 커밋과 작업 내용까지 모두 영구 삭제 (복구하려면 `git reflog` 필요)

`git revert [커밋해시]` : 해당 커밋을 취소하는 새 커밋을 생성 (기존 히스토리 유지, 이미 푸시된 커밋엔 이 방법 권장)

---

## 10. 고급 도구 (Advanced Tools)

`git stash` : 작업 중인 코드를 임시로 치워두고 깨끗한 상태로 전환

- `git stash` : 현재 작업(스테이징 + 수정) 임시 저장
- `git stash -u` : 추적되지 않는(Untracked) 새 파일까지 포함해서 임시 저장
- `git stash list` : 저장된 스태시 목록 확인 (`stash@{0}`, `stash@{1}` 형태로 표시)
- `git stash pop` : 가장 최근 스태시를 꺼내고 목록에서 삭제
- `git stash apply` : 스태시를 꺼내오기만 하고 목록에는 남겨둠 (여러 곳에 적용할 때 유용)
- `git stash drop` : 가장 최근 스태시 삭제
- `git stash clear` : 모든 스태시 기록 삭제

`git clean` : 추적되지 않는 파일(Untracked)을 강제 삭제

- `git clean -f` : 추적되지 않는 파일 강제 삭제
- `git clean -fd` : 추적되지 않는 파일과 디렉토리까지 모두 삭제
- `git clean -n` : 실제로 삭제하지 않고, 삭제 대상 목록만 미리 확인 (dry-run)

`git tag` : 특정 커밋에 버전 태그 달기 (주로 배포·릴리즈 시 사용)

- `git tag` : 태그 목록 조회
- `git tag [버전]` : 현재 커밋에 Lightweight 태그 생성 (예: `git tag v1.0.0`)
- `git tag -a [버전] -m "메시지"` : 작성자·날짜·설명이 포함된 Annotated 태그 생성 (배포 시 권장)
- `git push origin [태그명]` : 특정 태그 원격 업로드 (태그는 `git push`에 자동 포함 안 됨)
- `git push origin --tags` : 로컬의 모든 태그 원격 업로드
- `git tag -d [태그명]` : 로컬 태그 삭제
- `git push origin --delete [태그명]` : 원격 태그 삭제

---

## Commit Type 컨벤션

| 타입 | 설명 |
|------|------|
| `feat` | 새로운 기능 추가 |
| `fix` | 버그 수정 (잘못된 동작·오류 수정) |
| `refactor` | 코드 구조 개선 (기능 변경 없이 함수 분리, 중복 제거, 구조 효율화 등) |
| `style` | 코드 포맷팅·스타일 교정 (실행 결과에 영향 없는 변경, 세미콜론 추가 등) |
| `docs` | 문서·주석만 변경 (코드 수정 없음) |
| `test` | 테스트 코드 추가·수정·삭제 |
| `chore` | 기타 잡무, 빌드·설정 관리 (패키지 업데이트, `.gitignore` 수정 등) |
| `perf` | 성능 개선 |
| `ci` | CI/CD 설정 변경 (GitHub Actions, Dockerfile 등) |
| `revert` | 이전 커밋 되돌리기 |