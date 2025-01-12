# 米游社的API列表
BBS_COOKIE_URL = "https://webapi.account.mihoyo.com/Api/cookie_accountinfo_by_loginticket?login_ticket={}"
BBS_COOKIE_URL_2 = (
    "https://api-takumi.mihoyo.com/auth/api/getMultiTokenByLoginTicket?login_ticket={"
    "}&token_types=3&uid={}"
)
BBS_TASKS_LIST = "https://bbs-api.mihoyo.com/apihub/sapi/getUserMissionsState"
BBS_SIGN_URL = "https://bbs-api.mihoyo.com/apihub/app/api/signIn"
BBS_LIST_URL = (
    "https://bbs-api.mihoyo.com/post/api/getForumPostList?forum_id={"
    "}&is_good=false&is_hot=false&page_size=20&sort_type=1"
)
BBS_DETAIL_URL = "https://bbs-api.mihoyo.com/post/api/getPostFull?post_id={}"
BBS_SHARE_URL = "https://bbs-api.mihoyo.com/apihub/api/getShareConf?entity_id={}&entity_type=1"
BBS_LIKE_URL = "https://bbs-api.mihoyo.com/apihub/sapi/upvotePost"
BBS_API = "https://bbs-api.mihoyo.com"
BBS_CAPATCH = BBS_API + "/misc/api/createVerification?is_high=true"
BBS_CAPTCHA_VERIFY = BBS_API + "/misc/api/verifyVerification"

# 签到和米游币的salt
mihoyobbs_version = "2.46.1"  # Salt和Version相互对应
mihoyobbs_salt = "KZazpG4cO2QECFDBUCxdhS8cYCsQHfzn"
mihoyobbs_salt_web = "X7UOLLnTuNS3kgTJ1BUHOvKpiqp3kmym"
mihoyobbs_salt_x4 = "xV8v4Qu54lUKrEYFZkJhB8cuOh9Asafs"
mihoyobbs_salt_x6 = "t0qEgfub6cvueAPgR5m9aQWWVciEer7v"

# 米游社签到列表
mihoyo_bbs_List = [
    {
        "id": "1",
        "forumId": "1",
        "name": "崩坏3",
        "url": "https://bbs.mihoyo.com/bh3/",
    },
    {
        "id": "2",
        "forumId": "26",
        "name": "原神",
        "url": "https://bbs.mihoyo.com/ys/",
    },
    {
        "id": "3",
        "forumId": "30",
        "name": "崩坏2",
        "url": "https://bbs.mihoyo.com/bh2/",
    },
    {
        "id": "4",
        "forumId": "37",
        "name": "未定事件簿",
        "url": "https://bbs.mihoyo.com/wd/",
    },
    {
        "id": "5",
        "forumId": "34",
        "name": "大别野",
        "url": "https://bbs.mihoyo.com/dby/",
    },
    {
        "id": "6",
        "forumId": "52",
        "name": "崩坏：星穹铁道",
        "url": "https://bbs.mihoyo.com/sr/",
    },
    {
        "id": "8",
        "forumId": "57",
        "name": "绝区零",
        "url": "https://bbs.mihoyo.com/zzz/",
    },
]
