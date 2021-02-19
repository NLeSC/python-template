# Post generate hook for deleting unused files
# https://cookiecutter.readthedocs.io/en/1.7.2/advanced/hooks.html
import os

tweet_releases = '{{cookiecutter.tweet_releases}}' == 'yes'

if not tweet_releases:
    tweet_action_file = os.path.join(os.getcwd(), '.github/workflows/tweet-release.yml')
    os.remove(tweet_action_file)