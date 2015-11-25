import urllib2
import json

from django.conf import settings


def __get_response(url=None):
    if url is not None:
        request = urllib2.Request('{base_url}{url}&access_token={access_token}'.format(base_url=settings.REPO_URL, url=url,
                                                                          access_token=settings.GITHUB_TOKEN))
    else:
        request = urllib2.Request('{base_url}?access_token={access_token}'.format(base_url=settings.REPO_URL,access_token=settings.GITHUB_TOKEN))
    response = urllib2.urlopen(request).read()
    return response


def _get_user_info():
    user = json.loads(__get_response())['owner']
    return user


def _get_pr_list(url='/pulls?per_page=100'):
    pr_list = json.loads(__get_response(url))
    return pr_list


def _get_issues_list(url='/issues?per_page=100'):
    all_issues_list = json.loads(__get_response(url))
    issues_list = [item for item in all_issues_list if not 'pull_request' in item]
    return issues_list


def _get_contributors_list(url='/contributors?per_page=100'):
    contributors_list = json.loads(__get_response(url))
    return contributors_list


def collect_final_data():
    user = _get_user_info()
    repo = json.loads(__get_response())
    pr_list = _get_pr_list()
    issues_list = _get_issues_list()
    contributors_list = _get_contributors_list()
    return {
        'user': user,
        'repo': repo,
        'pr_list': pr_list,
        'issues_list': issues_list,
        'contributors_list': contributors_list,
    }