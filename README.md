# Linux & Terminal Practice

AI 엔지니어링 학습의 첫 단계로, [ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) Phase 0의 `10-terminal-and-shell`, `11-linux-for-ai` 레슨을 Ubuntu 24.04 VM(Multipass, Mac mini M4)에서 직접 따라 하며 정리했습니다.

## 환경
- Host: macOS (Apple Silicon)
- Guest: Ubuntu 24.04 (aarch64) via Multipass

## 직접 해 본 것
| 주제 | 내용 | 사용 명령어 |
|---|---|---|
| 권한 | 실행 권한 유무에 따른 `Permission denied` 확인, 숫자 표기(644/755) | `chmod`, `ls -l` |
| 프로세스·서비스 | 백그라운드 작업 확인·종료, SSH 서비스 상태 확인 | `jobs`, `ps aux`, `kill`, `systemctl status` |
| 디스크 | 500MB 더미 체크포인트 파일을 만들어 용량 증가 원인을 추적하고 정리 | `df -h`, `du -h`, `find -size`, `dd`, `rm` |
| tmux | 세션 생성, detach/attach로 작업 유지 | `tmux new/ls/attach` |
| 로그 처리 | 가짜 학습 로그에서 loss·acc 값 추출 및 정렬 | `grep`, `awk`, `sort`, `sed`, `wc` |
| 리다이렉트 | 정상 출력과 에러 출력 분리·병합, 화면 출력과 저장 동시 수행 | `>`, `>>`, `2>`, `2>&1`, `tee` |
| 백그라운드 실행 | 학습을 흉내 낸 스크립트를 실행하고 로그를 실시간 확인 | `nohup`, `&`, `tail -f`, `pkill` |

## 파일
- `fake_train.sh`: 1초마다 epoch와 loss를 출력하는 가짜 학습 스크립트
- `train.log`: 연습용 가짜 학습 로그 (랜덤 값)
- `command_history.txt`: 연습 중 실행한 명령어 기록

## 배운 점
- 오래 걸리는 작업은 `tmux`나 `nohup`으로 돌려야 접속이 끊겨도 유지된다.
- 디스크 문제는 `df`로 어느 디스크가 찼는지 보고, `du`와 `find`로 원인 폴더·파일을 좁혀 간다.
- 로그는 파이프(`grep | awk | sort`)로 필요한 값만 빠르게 뽑아 볼 수 있다.
