# data lake의 랭킹 정보를 가져와서, 등수를 업데이트 하는 코드
import json
import pandas as pd
import glob
from extract.helper import get_date

# 오늘 날짜 구하기
date = get_date(day='today')
all_dir = glob.glob('data/crawling/*')
directory = all_dir[0]
glob.glob(directory + '/*')
