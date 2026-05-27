# Youtube Upload Checker
video_length_mins = 40
is_exported = True
has_thumbnail = False
is_monetized = True

if not video_length_mins:
    print('No video found')
elif video_length_mins <= 5:
    if is_exported and has_thumbnail:
        print('Ready to upload')
    else:
        print('Not ready')
elif video_length_mins > 5 and video_length_mins <= 30:
    if is_exported and has_thumbnail and is_monetized:
        print('Ready to upload')
    else:
        print('Not ready')
else:
    if video_length_mins > 30:
        print('Too long for standard upload')
    else:
        print('Ready to upload')