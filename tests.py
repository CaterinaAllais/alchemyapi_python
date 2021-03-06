#!/usr/bin/env python
from __future__ import print_function
from alchemyapi import AlchemyAPI


test_text = 'Bob broke my heart, and then made up this silly sentence to test the PHP SDK'  
test_html = '<html><head><title>The best SDK Test | AlchemyAPI</title></head><body><h1>Hello World!</h1><p>My favorite language is PHP</p></body></html>'
test_url = 'http://www.nytimes.com/2013/07/13/us/politics/a-day-of-friction-notable-even-for-a-fractious-congress.html?_r=0'



alchemyapi = AlchemyAPI()


#Entities
print('Checking entities . . . ')
response = alchemyapi.entities('text', test_text);
assert(response['status'] == 'OK')
response = alchemyapi.entities('html', test_html);
assert(response['status'] == 'OK')
response = alchemyapi.entities('url', test_url);
assert(response['status'] == 'OK')
response = alchemyapi.entities('random', test_url);
assert(response['status'] == 'ERROR') 	#invalid flavor
print('Entity tests complete!')
print('')


#Keywords
print('Checking keywords . . . ')
response = alchemyapi.keywords('text', test_text);
assert(response['status'] == 'OK')
response = alchemyapi.keywords('html', test_html);
assert(response['status'] == 'OK')
response = alchemyapi.keywords('url', test_url);
assert(response['status'] == 'OK')
response = alchemyapi.keywords('random', test_url);
assert(response['status'] == 'ERROR') 	#invalid flavor
print('Keyword tests complete!')
print('')




#Concepts
print('Checking concepts . . . ')
response = alchemyapi.concepts('text', test_text);
assert(response['status'] == 'OK')
response = alchemyapi.concepts('html', test_html);
assert(response['status'] == 'OK')
response = alchemyapi.concepts('url', test_url);
assert(response['status'] == 'OK')
response = alchemyapi.concepts('random', test_url);
assert(response['status'] == 'ERROR') 	#invalid flavor
print('Concept tests complete!')
print('')



#Sentiment
print('Checking sentiment . . . ')
response = alchemyapi.sentiment('text', test_text);
assert(response['status'] == 'OK')
response = alchemyapi.sentiment('html', test_html);
assert(response['status'] == 'OK')
response = alchemyapi.sentiment('url', test_url);
assert(response['status'] == 'OK')
response = alchemyapi.sentiment('random', test_url);
assert(response['status'] == 'ERROR') 	#invalid flavor
print('Sentiment tests complete!')
print('')



#Targeted Sentiment
print('Checking targeted sentiment . . . ')
response = alchemyapi.sentiment_targeted('text', test_text, 'heart');
assert(response['status'] == 'OK')
response = alchemyapi.sentiment_targeted('html', test_html, 'language');
assert(response['status'] == 'OK')
response = alchemyapi.sentiment_targeted('url', test_url, 'Congress');
assert(response['status'] == 'OK')
response = alchemyapi.sentiment_targeted('random', test_url, 'Congress');
assert(response['status'] == 'ERROR') 	#invalid flavor
response = alchemyapi.sentiment_targeted('text', test_text,  None);
assert(response['status'] == 'ERROR') 	#missing target
print('Targeted sentiment tests complete!')
print('')



#Text
print('Checking text . . . ')
response = alchemyapi.text('text', test_text);
assert(response['status'] == 'ERROR')	#only works for html and url content
response = alchemyapi.text('html', test_html);
assert(response['status'] == 'OK')
response = alchemyapi.text('url', test_url);
assert(response['status'] == 'OK')
print('Text tests complete!')
print('')



#Text Raw
print('Checking raw text . . . ')
response = alchemyapi.text_raw('text', test_text);
assert(response['status'] == 'ERROR')	#only works for html and url content
response = alchemyapi.text_raw('html', test_html);
assert(response['status'] == 'OK')
response = alchemyapi.text_raw('url', test_url);
assert(response['status'] == 'OK')
print('Raw text tests complete!')
print('')



#Author
print('Checking author . . . ')
response = alchemyapi.author('text', test_text);
assert(response['status'] == 'ERROR')	#only works for html and url content
response = alchemyapi.author('html', test_html);
assert(response['status'] == 'ERROR')	#there's no author in the test HTML
response = alchemyapi.author('url', test_url);
assert(response['status'] == 'OK')
print('Author tests complete!')
print('')



#Language
print('Checking language . . . ')
response = alchemyapi.language('text', test_text);
assert(response['status'] == 'OK')
response = alchemyapi.language('html', test_html);
assert(response['status'] == 'OK')
response = alchemyapi.language('url', test_url);
assert(response['status'] == 'OK')
response = alchemyapi.language('random', test_url);
assert(response['status'] == 'ERROR') 	#invalid flavor
print('Language tests complete!')
print('')



#Title
print('Checking title . . . ')
response = alchemyapi.title('text', test_text);
assert(response['status'] == 'ERROR')	#only works for html and url content
response = alchemyapi.title('html', test_html);
assert(response['status'] == 'OK')
response = alchemyapi.title('url', test_url);
assert(response['status'] == 'OK')
print('Title tests complete!')
print('')



#Relations
print('Checking relations . . . ')
response = alchemyapi.relations('text', test_text);
assert(response['status'] == 'OK')
response = alchemyapi.relations('html', test_html);
assert(response['status'] == 'OK')
response = alchemyapi.relations('url', test_url);
assert(response['status'] == 'OK')
response = alchemyapi.relations('random', test_url);
assert(response['status'] == 'ERROR') 	#invalid flavor
print('Relation tests complete!')
print('')



#Category
print('Checking category . . . ')
response = alchemyapi.category('text', test_text);
assert(response['status'] == 'OK')
response = alchemyapi.category('html', test_html, {'url':'test'});
assert(response['status'] == 'OK')
response = alchemyapi.category('url', test_url);
assert(response['status'] == 'OK')
response = alchemyapi.category('random', test_url);
assert(response['status'] == 'ERROR') 	#invalid flavor
print('Category tests complete!')
print('')



#Feeds
print('Checking feeds . . . ')
response = alchemyapi.feeds('text', test_text);
assert(response['status'] == 'ERROR')	#only works for html and url content
response = alchemyapi.feeds('html', test_html, {'url':'test'});
assert(response['status'] == 'OK')
response = alchemyapi.feeds('url', test_url);
assert(response['status'] == 'OK')
print('Feed tests complete!')
print('')



#Microformats
print('Checking microformats . . . ')
response = alchemyapi.microformats('text', test_text);
assert(response['status'] == 'ERROR')	#only works for html and url content
response = alchemyapi.microformats('html', test_html, {'url':'test'});
assert(response['status'] == 'OK')
response = alchemyapi.microformats('url', test_url);
assert(response['status'] == 'OK')
print('Microformat tests complete!')
print('')
print('')


print('**** All tests complete! ****')



