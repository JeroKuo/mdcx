import time


# This file was automatically generated by src/models/config_generator.py.
# Don't modify it manually.

class GeneratedConfig:
    """
    Auto generated configuration
    Also used as default configuration
    """
    # modified_time
    modified_time = r'2024-03-07 20:03:00'
    version = 120240308

    # media
    media_path = r''
    softlink_path = r'softlink'
    success_output_folder = r'JAV_output'
    failed_output_folder = r'failed'
    extrafanart_folder = r'extrafanart_copy'
    media_type = r'.mp4|.avi|.rmvb|.wmv|.mov|.mkv|.flv|.ts|.webm|.iso|.mpg'
    sub_type = r'.smi|.srt|.idx|.sub|.sup|.psb|.ssa|.ass|.usf|.xss|.ssf|.rt|.lrc|.sbv|.vtt|.ttml'
    scrape_softlink_path = r''
    auto_link = 0

    # escape
    folders = r'JAV_output,examples'
    string = r'h_720,2048论坛@fun2048.com,1080p,720p,22-sht.me,-HD,bbs2048.org@,hhd800.com@,icao.me@,hhb_000,[456k.me],[ThZu.Cc]'
    file_size = 100.0
    no_escape = r'record_success_file,'

    # clean
    clean_ext = r'.html|.url'
    clean_name = r'uur76.mp4|uur9 3.com.mp4'
    clean_contains = r'直 播 盒 子|最 新 情 報|最 新 位 址|注册免费送|房间火爆|美女荷官|妹妹直播|精彩直播'
    clean_size = 0.0
    clean_ignore_ext = r''
    clean_ignore_contains = r'skip|ignore'
    clean_enable = r'clean_ext,clean_name,clean_contains,clean_size,clean_ignore_ext,clean_ignore_contains,'

    # common
    thread_number = 10
    thread_time = 0
    javdb_time = 10
    main_mode = 1
    read_mode = r''
    update_mode = r'c'
    update_a_folder = r'actor'
    update_b_folder = r'number actor'
    update_d_folder = r'number actor'
    soft_link = 0
    success_file_move = 1
    failed_file_move = 1
    success_file_rename = 1
    del_empty_folder = 1
    show_poster = 1

    # file_download
    download_files = r',poster,thumb,fanart,nfo,ignore_wuma,ignore_fc2,ignore_guochan,'
    keep_files = r',extrafanart,trailer,theme_videos,'
    download_hd_pics = r'poster,thumb,amazon,official,google,'
    google_used = r'm.media-amazon.com,'
    google_exclude = r'fake,javfree,idoljp.com,qqimg.top,u9a9,picturedata,abpic,pbs.twimg.com,naiwarp'

    # website
    scrape_like = r'info'
    website_single = r'airav_cc'
    website_youma = r'airav_cc,iqqtv,javbus,freejavbt,jav321,dmm,javlibrary,7mmtv,hdouban,javdb,avsex,lulubar,airav,xcity,avsox'
    website_wuma = r'iqqtv,javbus,freejavbt,jav321,avsox,7mmtv,hdouban,javdb,airav'
    website_suren = r'mgstage,avsex,jav321,freejavbt,7mmtv,javbus,javdb'
    website_fc2 = r'fc2,fc2club,fc2hub,freejavbt,7mmtv,hdouban,javdb,avsox,airav'
    website_oumei = r'theporndb,javdb,javbus,hdouban'
    website_guochan = r'madouqu,mdtv,hdouban,cnmdb'
    whole_fields = r'outline,actor,thumb,release,tag,'
    none_fields = r'wanted,'
    website_set = r'official,'
    title_website = r'theporndb,mgstage,dmm,javbus,jav321,javlibrary'
    title_zh_website = r'airav_cc,iqqtv,avsex,lulubar'
    title_website_exclude = r''
    outline_website = r'theporndb,dmm,jav321'
    outline_zh_website = r'airav_cc,avsex,iqqtv,lulubar'
    outline_website_exclude = r'avsox,fc2club,javbus,javdb,javlibrary,freejavbt,hdouban'
    actor_website = r'theporndb,javbus,javlibrary,javdb'
    actor_website_exclude = r''
    thumb_website = r'theporndb,javbus'
    thumb_website_exclude = r'javdb'
    poster_website = r'theporndb,avsex,javbus'
    poster_website_exclude = r'airav,fc2club,fc2hub,iqqtv,7mmtv,javlibrary,lulubar'
    extrafanart_website = r'javbus,freejavbt'
    extrafanart_website_exclude = r'airav,airav_cc,avsex,avsox,iqqtv,javlibrary,lulubar'
    trailer_website = r'freejavbt,mgstage,dmm'
    trailer_website_exclude = r'7mmtv,lulubar'
    tag_website = r'javbus,freejavbt'
    tag_website_exclude = r''
    release_website = r'javbus,freejavbt,7mmtv'
    release_website_exclude = r'fc2club,fc2hub'
    runtime_website = r'javbus,freejavbt'
    runtime_website_exclude = r'airav,airav_cc,fc2,fc2club,fc2hub,lulubar'
    score_website = r'jav321,javlibrary,javdb'
    score_website_exclude = r'airav,airav_cc,avsex,avsox,7mmtv,fc2,fc2hub,iqqtv,javbus,xcity,lulubar'
    director_website = r'javbus,freejavbt'
    director_website_exclude = r'airav,airav_cc,avsex,avsox,fc2,fc2hub,iqqtv,jav321,mgstage,lulubar'
    series_website = r'javbus,freejavbt'
    series_website_exclude = r'airav,airav_cc,avsex,iqqtv,7mmtv,javlibrary,lulubar'
    studio_website = r'javbus,freejavbt'
    studio_website_exclude = r'avsex'
    publisher_website = r'javbus'
    publisher_website_exclude = r'airav,airav_cc,avsex,iqqtv,lulubar'
    wanted_website = r'javlibrary,javdb'
    translate_by = r'youdao,google,deepl,'
    deepl_key = r''
    title_language = r'zh_cn'
    title_sehua = r'on'
    title_yesjav = r'off'
    title_translate = r'on'
    title_sehua_zh = r'on'
    outline_language = r'zh_cn'
    outline_translate = r'on'
    outline_show = r''
    actor_language = r'zh_cn'
    actor_realname = r'on'
    actor_translate = r'on'
    tag_language = r'zh_cn'
    tag_translate = r'on'
    tag_include = r'actor,letters,series,studio,publisher,cnword,mosaic,definition,'
    director_language = r'zh_cn'
    director_translate = r'on'
    series_language = r'zh_cn'
    series_translate = r'on'
    studio_language = r'zh_cn'
    studio_translate = r'on'
    publisher_language = r'zh_cn'
    publisher_translate = r'on'
    nfo_include_new = r'sorttitle,originaltitle,title_cd,outline,plot_,originalplot,release_,releasedate,premiered,country,mpaa,customrating,year,runtime,wanted,score,criticrating,actor,director,series,tag,genre,series_set,studio,maker,publisher,label,poster,cover,trailer,website,'
    nfo_tagline = r'发行日期 release'
    nfo_tag_series = r'系列: series'
    nfo_tag_studio = r'片商: studio'
    nfo_tag_publisher = r'发行: publisher'

    # Name_Rule
    folder_name = r'actor/number actor'
    naming_file = r'number'
    naming_media = r'number title'
    prevent_char = r''
    fields_rule = r'del_actor,del_char,'
    suffix_sort = r'mosaic,cnword'
    actor_no_name = r'未知演员'
    release_rule = r'YYYY-MM-DD'
    folder_name_max = 60
    file_name_max = 60
    actor_name_max = 3
    actor_name_more = r'等演员'
    umr_style = r'-破解'
    leak_style = r'-流出'
    wuma_style = r''
    youma_style = r''
    show_moword = r'file,'
    show_4k = r'folder,file,'
    cd_name = 0
    cd_char = r'letter,underline,'
    pic_name = 0
    trailer_name = 1
    hd_name = r'height'
    hd_get = r'video'

    # subtitle
    cnword_char = r'-C.,-C-,ch.,字幕'
    cnword_style = r'^-C^'
    folder_cnword = r'on'
    file_cnword = r'on'
    subtitle_folder = r''
    subtitle_add = r'off'
    subtitle_add_chs = r'on'
    subtitle_add_rescrape = r'on'

    # emby
    server_type = r'emby'
    emby_url = r'http://192.168.5.191:8096'
    api_key = r'ee9a2f2419704257b1dd60b975f2d64e'
    user_id = r''
    emby_on = r'actor_info_zh_cn,actor_info_miss,actor_photo_net,actor_photo_miss,'
    use_database = 0
    info_database_path = r''
    gfriends_github = r'https://github.com/gfriends/gfriends'
    actor_photo_folder = r''
    actor_photo_kodi_auto = 0

    # mark
    poster_mark = 1
    thumb_mark = 1
    fanart_mark = 0
    mark_size = 5
    mark_type = r'sub,umr,leak,uncensored,hd'
    mark_fixed = r'off'
    mark_pos = r'top_left'
    mark_pos_corner = r'top_left'
    mark_pos_sub = r'top_left'
    mark_pos_mosaic = r'top_right'
    mark_pos_hd = r'bottom_right'

    # proxy
    type = r'no'
    proxy = r'127.0.0.1:7890'
    timeout = 10
    retry = 3
    theporndb_api_token = r''

    # Cookies
    javdb = r''
    javbus = r''

    # other
    show_web_log = r'off'
    show_from_log = r'on'
    show_data_log = r'on'
    save_log = r'on'
    update_check = r'on'
    local_library = r''
    actors_name = r''
    netdisk_path = r''
    localdisk_path = r''
    window_title = r'hide'
    switch_on = r'rest_scrape,remain_task,show_dialog_stop_scrape,show_logs,ipv4_only,hide_none,'
    timed_interval = r'00:30:00'
    rest_count = 20
    rest_time = r'00:01:02'
    statement = 3
    CONFIG_STR = f"""
[modified_time]
modified_time = {time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())}
version = {version}

[media]
media_path = {media_path}
softlink_path = {softlink_path}
success_output_folder = {success_output_folder}
failed_output_folder = {failed_output_folder}
extrafanart_folder = {extrafanart_folder}
media_type = {media_type}
sub_type = {sub_type}
scrape_softlink_path = {scrape_softlink_path}

[escape]
folders = {folders}
string = {string}
file_size = {file_size}
no_escape = {no_escape}

[clean]
clean_ext = {clean_ext}
clean_name = {clean_name}
clean_contains = {clean_contains}
clean_size = {clean_size}
clean_ignore_ext = {clean_ignore_ext}
clean_ignore_contains = {clean_ignore_contains}
clean_enable = {clean_enable}

[common]
thread_number = {thread_number}
thread_time = {thread_time}
javdb_time = {javdb_time}
main_mode = {main_mode}
read_mode = {read_mode}
update_mode = {update_mode}
update_a_folder = {update_a_folder}
update_b_folder = {update_b_folder}
update_d_folder = {update_d_folder}
soft_link = {soft_link}
success_file_move = {success_file_move}
failed_file_move = {failed_file_move}
success_file_rename = {success_file_rename}
del_empty_folder = {del_empty_folder}
show_poster = {show_poster}

[file_download]
download_files = {download_files}
keep_files = {keep_files}
download_hd_pics = {download_hd_pics}
google_used = {google_used}
google_exclude = {google_exclude}

[website]
scrape_like = {scrape_like}
website_single = {website_single}
website_youma = {website_youma}
website_wuma = {website_wuma}
website_suren = {website_suren}
website_fc2 = {website_fc2}
website_oumei = {website_oumei}
website_guochan = {website_guochan}
whole_fields = {whole_fields}
none_fields = {none_fields}
website_set = {website_set}
title_website = {title_website}
title_zh_website = {title_zh_website}
title_website_exclude = {title_website_exclude}
outline_website = {outline_website}
outline_zh_website = {outline_zh_website}
outline_website_exclude = {outline_website_exclude}
actor_website = {actor_website}
actor_website_exclude = {actor_website_exclude}
thumb_website = {thumb_website}
thumb_website_exclude = {thumb_website_exclude}
poster_website = {poster_website}
poster_website_exclude = {poster_website_exclude}
extrafanart_website = {extrafanart_website}
extrafanart_website_exclude = {extrafanart_website_exclude}
trailer_website = {trailer_website}
trailer_website_exclude = {trailer_website_exclude}
tag_website = {tag_website}
tag_website_exclude = {tag_website_exclude}
release_website = {release_website}
release_website_exclude = {release_website_exclude}
runtime_website = {runtime_website}
runtime_website_exclude = {runtime_website_exclude}
score_website = {score_website}
score_website_exclude = {score_website_exclude}
director_website = {director_website}
director_website_exclude = {director_website_exclude}
series_website = {series_website}
series_website_exclude = {series_website_exclude}
studio_website = {studio_website}
studio_website_exclude = {studio_website_exclude}
publisher_website = {publisher_website}
publisher_website_exclude = {publisher_website_exclude}
wanted_website = {wanted_website}
translate_by = {translate_by}
deepl_key = {deepl_key}
title_language = {title_language}
title_sehua = {title_sehua}
title_yesjav = {title_yesjav}
title_translate = {title_translate}
title_sehua_zh = {title_sehua_zh}
outline_language = {outline_language}
outline_translate = {outline_translate}
outline_show = {outline_show}
actor_language = {actor_language}
actor_realname = {actor_realname}
actor_translate = {actor_translate}
tag_language = {tag_language}
tag_translate = {tag_translate}
tag_include = {tag_include}
director_language = {director_language}
director_translate = {director_translate}
series_language = {series_language}
series_translate = {series_translate}
studio_language = {studio_language}
studio_translate = {studio_translate}
publisher_language = {publisher_language}
publisher_translate = {publisher_translate}
nfo_include_new = {nfo_include_new}
nfo_tagline = {nfo_tagline}
nfo_tag_series = {nfo_tag_series}
nfo_tag_studio = {nfo_tag_studio}
nfo_tag_publisher = {nfo_tag_publisher}
# website: iqqtv, javbus, javdb, freejavbt, jav321, dmm, avsox, xcity, mgstage, fc2, fc2club, fc2hub, airav, javlibrary, mdtv

[Name_Rule]
folder_name = {folder_name}
naming_file = {naming_file}
naming_media = {naming_media}
prevent_char = {prevent_char}
fields_rule = {fields_rule}
suffix_sort = {suffix_sort}
actor_no_name = {actor_no_name}
release_rule = {release_rule}
folder_name_max = {folder_name_max}
file_name_max = {file_name_max}
actor_name_max = {actor_name_max}
actor_name_more = {actor_name_more}
umr_style = {umr_style}
leak_style = {leak_style}
wuma_style = {wuma_style}
youma_style = {youma_style}
show_moword = {show_moword}
show_4k = {show_4k}
cd_name = {cd_name}
cd_char = {cd_char}
pic_name = {pic_name}
trailer_name = {trailer_name}
hd_name = {hd_name}
hd_get = {hd_get}
# 命名字段有：title, originaltitle, actor, number, studio, publisher, year, mosaic, runtime, director, release, series, definition, cnword

[subtitle]
cnword_char = {cnword_char}
cnword_style = {cnword_style}
folder_cnword = {folder_cnword}
file_cnword = {file_cnword}
subtitle_folder = {subtitle_folder}
subtitle_add = {subtitle_add}
subtitle_add_chs = {subtitle_add_chs}
subtitle_add_rescrape = {subtitle_add_rescrape}

[emby]
server_type = {server_type}
emby_url = {emby_url}
api_key = {api_key}
emby_on = {emby_on}
use_database = {use_database}
info_database_path = {info_database_path}
gfriends_github = {gfriends_github}
actor_photo_folder = {actor_photo_folder}

[mark]
poster_mark = {poster_mark}
thumb_mark = {thumb_mark}
fanart_mark = {fanart_mark}
mark_size = {mark_size}
mark_type = {mark_type}
mark_fixed = {mark_fixed}
mark_pos = {mark_pos}
mark_pos_corner = {mark_pos_corner}
mark_pos_sub = {mark_pos_sub}
mark_pos_mosaic = {mark_pos_mosaic}
mark_pos_hd = {mark_pos_hd}
# mark_size: range 1-40
# mark_type: sub, youma, umr, leak, uncensored, hd
# mark_pos: top_left, top_right, bottom_left, bottom_right

[proxy]
type = {type}
proxy = {proxy}
timeout = {timeout}
retry = {retry}
theporndb_api_token = {theporndb_api_token}
# type: no, http, socks5

[Cookies]
javdb = {javdb}
javbus = {javbus}
# cookies存在有效期，记得更新

[other]
show_web_log = {show_web_log}
show_from_log = {show_from_log}
show_data_log = {show_data_log}
save_log = {save_log}
update_check = {update_check}
local_library = {local_library}
actors_name = {actors_name}
netdisk_path = {netdisk_path}
localdisk_path = {localdisk_path}
window_title = {window_title}
switch_on = {switch_on}
timed_interval = {timed_interval}
rest_count = {rest_count}
rest_time = {rest_time}
statement = {statement}"""
