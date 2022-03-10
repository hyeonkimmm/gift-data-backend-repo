# data lake의 랭킹 정보를 가져와서, 등수를 업데이트 하는 코드
import glob
import pandas as pd
from extract.helper import get_date
# from collections import defaultdict
def get_top5_rank(path):
    df = pd.read_csv(path)
    return df
def delete_file(directory, file_name='/score.csv'):
    '''
    파일 잘못 만들었을 경우 삭제하기 위한 임시 삭제 코드
    '''
    import os
    score = glob.glob(directory + f'{file_name}')
    if score:
        file_path = score[0]
        if os.path.isfile(file_path):
            os.remove(file_path)

def calculation_score(directory):
    info = directory.split('\\')[-1]
    # age, gender, c_id, c_name = info.split('_')
    file_list = glob.glob(directory + '/2*')
    score = glob.glob(directory + '/score.csv')
    try:
        if score:
            # 스코어 값이 있기 때문에 가장 최근 것만 추가
            merge_df = pd.read_csv(score[0])
            # 파일이 어제 일자가 아니면 적용 X
            update_date = file_list[-1].split('\\')[-1].split('_')[0]
            yesterday_date = get_date(day='yesterday')
            if update_date == yesterday_date:
                data = pd.read_csv(file_list[-1])
                data['score_'] = data['rank'].apply(lambda x: 21 - x)
                data = data[['keyword', 'score_']]
                merge_df = pd.merge(merge_df, data, how='right', on='keyword').fillna(0)
                merge_df['score'] = merge_df[['score', 'score_']].apply(lambda x: x[0] + x[1], axis=1)
                merge_df = merge_df[['keyword', 'score']].sort_values(by='score', ascending=False)
                merge_df.to_csv(path_or_buf=f'{directory}/score.csv', index=False)
            else:
                print(f'Data has not been updated.{info}')
                return
        else:
            # 스코어 값이 없기 때문에 모든 file 추가
            file_path = file_list[0]
            data = pd.read_csv(file_path)
            data['score'] = data['rank'].apply(lambda x: 21 - x)
            merge_df = data[['keyword', 'score']]
            for file_path in file_list[1:]:
                data = pd.read_csv(file_path)
                data['score_'] = data['rank'].apply(lambda x: 21 - x)
                data = data[['keyword', 'score_']]
                merge_df = pd.merge(merge_df, data, how='right', on='keyword').fillna(0)
                merge_df['score'] = merge_df[['score', 'score_']].apply(lambda x: x[0] + x[1], axis=1)
                merge_df = merge_df[['keyword', 'score']].sort_values(by='score', ascending=False)
                merge_df.to_csv(path_or_buf=f'{directory}/score.csv', index=False)
    except Exception:
        print(f'error occurred! {info}')
    else:
        print(f'finish calculated to {info}')


# 오늘 날짜
# date = get_date(day='today')

if __name__ == '__main__':
    # score 업데이트
    all_dir = glob.glob('data/crawling/*')
    # 디렉토리 반복
    for directory in all_dir:
        calculation_score(directory)

'''
 result = pd.read_csv(file_list[-1])
# get top5
result = result.iloc[:5, :].copy()
result.loc[:, 'age'] = age
result.loc[:, 'gender'] = gender
result.loc[:, 'c_id'] = c_id
result.loc[:, 'c_name'] = c_name
result.loc[:, 'date'] = date
result = result[['date', 'rank', 'age', 'gender', 'c_id', 'c_name', 'keyword']]
'''
