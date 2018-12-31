from thumbnail_maker_queue import ThumbnailMakerService

IMG_URLS = \
    ['https://photo.tuchong.com/461036/f/400228599.jpg',
     'https://photo.tuchong.com/461036/f/50528830.jpg',
     'https://photo.tuchong.com/461036/f/7991721.jpg',
     'https://photo.tuchong.com/461036/f/583271888.jpg',
     'https://photo.tuchong.com/461036/f/568591729.jpg',
     'https://photo.tuchong.com/461036/f/308085784.jpg',
     'https://photo.tuchong.com/461036/f/627376253.jpg',
     'https://photo.tuchong.com/461036/f/7978286.jpg',
     'https://photo.tuchong.com/461036/f/7976932.jpg',
     'https://photo.tuchong.com/461036/f/7978127.jpg',
     'https://photo.tuchong.com/461036/f/613285995.jpg',
     'https://photo.tuchong.com/461036/f/7977751.jpg',
     'https://photo.tuchong.com/461036/f/576586220.jpg',
     'https://photo.tuchong.com/461036/f/333054500.jpg',
     'https://photo.tuchong.com/461036/f/7977518.jpg'
    ]
    
tn_maker = ThumbnailMakerService()
tn_maker.make_thumbnails(IMG_URLS)
