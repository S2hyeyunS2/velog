import feedparser
import git
import os

# 벨로그 RSS 피드 URL
rss_url = 'https://api.velog.io/rss/hyeyun98'

# 깃허브 레포지토리 경로
repo_path = '.'

# 'velog-posts' 폴더 경로
posts_dir = os.path.join(repo_path, 'velog-posts')

# 'velog-posts' 폴더가 없다면 생성
if not os.path.exists(posts_dir):
    os.makedirs(posts_dir)

# 레포지토리 로드
repo = git.Repo(repo_path)

# RSS 피드 파싱
feed = feedparser.parse(rss_url)

# 각 글을 파일로 저장하고 커밋
for entry in feed.entries:
    file_name = entry.title.replace('/', '-').replace('\\', '-') + '.md'
    file_path = os.path.join(posts_dir, file_name)

    # 파일이 없을 경우만 생성
    if not os.path.exists(file_path):
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(entry.description)

        # 깃허브 커밋
        repo.git.add(file_path)
        repo.git.commit('-m', f'Add post: {entry.title}')

# ✅ GitHub Actions에서 `git push`를 실행하므로 Python에서 push() 호출 제거
