''' actor serializer '''
from fedireads.settings import DOMAIN

def get_actor(user):
    ''' activitypub actor from db User '''
    avatar = user.avatar

    icon_path = '/static/images/default_avi.jpg'
    icon_type = 'image/jpeg'
    if avatar:
        icon_path = avatar.url
        icon_type = 'image/%s' % icon_path.split('.')[-1]

    icon_url = 'https://%s%s' % (DOMAIN, icon_path)
    return {
        '@context': [
            'https://www.w3.org/ns/activitystreams',
            'https://w3id.org/security/v1',
            {
                "manuallyApprovesFollowers": "as:manuallyApprovesFollowers",
                "schema": "http://schema.org#",
                "PropertyValue": "schema:PropertyValue",
                "value": "schema:value",
            },
        ],

        'id': user.actor,
        'type': 'Person',
        'preferredUsername': user.localname,
        'name': user.name,
        'inbox': user.inbox,
        'outbox': '%s/outbox' % user.actor,
        'followers': '%s/followers' % user.actor,
        'following': '%s/following' % user.actor,
        'summary': user.summary,
        'publicKey': {
            'id': '%s/#main-key' % user.actor,
            'owner': user.actor,
            'publicKeyPem': user.public_key,
        },
        'endpoints': {
            'sharedInbox': user.shared_inbox,
        },
        'fedireadsUser': True,
        'manuallyApprovesFollowers': user.manually_approves_followers,
        "icon": {
            "type": "Image",
            "mediaType": icon_type,
            "url": icon_url,
        },
    }
