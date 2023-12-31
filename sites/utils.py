from googleapiclient.discovery import build
import requests
from learnstack.settings.base import UDEMY_ACCESS_TOKEN, YOUTUBE_API_KEY
from sites.models import UdemyCourse, YouTubeVideo
from django.core.cache import cache


YOUTUBE_MAX_RESULTS = 25
UDEMY_PAGE_SIZE = 25


def search_youtube_videos(query, search_query):
    youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)
    search_response = youtube.search().list(
        q=query,
        part='snippet',
        maxResults=YOUTUBE_MAX_RESULTS
    ).execute()


    results = []
    for search_result in search_response.get('items', []):
        video_id = search_result.get('id', {}).get('videoId', '')
        title = search_result.get('snippet', {}).get('title', '')
        description = search_result.get('snippet', {}).get('description', '')
        thumbnails = search_result.get('snippet', {}).get('thumbnails', {})
        thumbnail_url = (
            thumbnails.get('maxres', {}).get('url', '') or
            thumbnails.get('high', {}).get('url', '') or
            thumbnails.get('default', {}).get('url', '')
        )

        YouTubeVideo.objects.create(search_query=search_query, video_id=video_id, title=title, description=description,thumbnail_url=thumbnail_url)

        result = {
            'video_id': video_id,
            'title': title,
            'description': description,
            'thumbnail_url': thumbnail_url,
        }
        results.append(result)

    return results

def search_udemy_courses(query, search_query):
    access_token = UDEMY_ACCESS_TOKEN
    search_url = f'https://www.udemy.com/api-2.0/courses/?search={query}&page_size={UDEMY_PAGE_SIZE}'
    headers = {'Authorization': f'Bearer {access_token}'}
    search_response = requests.get(search_url, headers=headers)

    if search_response.status_code == 200:
        results = []
        api_results = search_response.json().get('results')

        for api_result in api_results:
            title = api_result.get('title')
            price = api_result.get('price')
            thumbnail = api_result.get('image_480x270')
            url = api_result.get('url')

            UdemyCourse.objects.create(search_query=search_query, title=title, thumbnail=thumbnail, link=url,price=price)

            result = {
                'title': title,
                'price': price,
                'thumbnail': thumbnail,
                'url': url,
            }
            results.append(result)
        return results