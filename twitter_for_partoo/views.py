from pyramid.view import view_config
import pyramid.httpexceptions as exc

from TwitterAPI import TwitterAPI, TwitterRestPager


CONSUMER_KEY = 'himvY86y3TkFQzohDlTlyACyw'
CONSUMER_SECRET = 'ilUY9Du7EUGph2j4u1hwlgrMl42feKQtCHXiQDJsOF1uPcOy2m'
ACCESS_TOKEN_KEY = '36914429-cac9P5yXEXtVaGTUFVmdYiLdwq58aem0v3U2bSMij'
ACCESS_TOKEN_SECRET = 'bFapLrbOpZbFPLzXHggl58NySI9DzSKmFT4QZuCy06ziy'


api = TwitterAPI(CONSUMER_KEY,
                 CONSUMER_SECRET,
                 ACCESS_TOKEN_KEY,
                 ACCESS_TOKEN_SECRET,
                 auth_type='oAuth1',
                 proxy_url=None)



@view_config(route_name='home', renderer='templates/mytemplate.pt')
def my_view(request):

    #Get last 10 tweets on my timeline
    tweets = api.request('statuses/home_timeline', {'count':10})

    return {'project': 'twitter_for_partoo', 'tweets': tweets}


@view_config(route_name='newtweet')
def newtweet(request):

    # Post a tweet
    TWEET_TEXT = "Partoo is the best Product to make your business known!"
    api.request('statuses/update', {'status': TWEET_TEXT})

    raise exc.HTTPSeeOther('/')

