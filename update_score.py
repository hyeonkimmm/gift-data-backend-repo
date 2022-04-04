# data lake의 랭킹 정보를 가져와서, 등수를 업데이트 하는 코드
import glob
import pandas as pd
import os
def get_top_rank(path, top_rank=None):
    df = pd.read_csv(path)
    if top_rank is None:
        return df
    else:
        return df[:top_rank]
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

def is_file(_path, file_name='update_date.txt'):
    return os.path.isfile(_path + '/' + file_name)

def get_update_date(path):
    update_path = path + '/update_date.txt'
    f = open(update_path, 'r')
    update_date = f.readline()
    f.close()
    return update_date

def set_update_date(path, update_date):
    update_path = path + '/update_date.txt'
    f = open(update_path, 'w')
    f.write(update_date)
    f.close()

def apply_score(path, merge_df):
    data = pd.read_csv(path)
    data['score_'] = data['rank'].apply(lambda x: 21 - x)
    data = data[['keyword', 'score_']]
    merge_df = pd.merge(merge_df, data, how='outer', on='keyword').fillna(0)
    merge_df['score'] = merge_df[['score', 'score_']].apply(lambda x: x[0] + x[1], axis=1)
    merge_df = merge_df[['keyword', 'score']].sort_values(by='score', ascending=False)
    return merge_df

def calculation_score(directory):
    info = directory.split('\\')[-1]
    # age, gender, c_id, c_name = info.split('_')
    file_list = glob.glob(directory + '/2*')
    score = glob.glob(directory + '/score.csv')
    try:
        if is_file(_path=directory, file_name='score.csv'):
            # 스코어 값이 있기 때문에 가장 최근 것만 추가
            merge_df = pd.read_csv(score[0])
            extract_update_date = file_list[-1].split('\\')[-1].split('_')[0]
            # 파일이 어제 일자가 아니면 적용 X
            # 최종 업데이트 날짜 개별적용
            if is_file(_path=directory, file_name='update_date.txt'):
                # update 파일이 있을 때
                last_update_date = get_update_date(directory)
                # 멱등성 만족
                if last_update_date > extract_update_date:
                    # 최종 업데이트 날짜와 파일 상의 날짜 비교
                    # 이미 업데이트 되었으므로 업데이트 하지 않음
                    print(f'already updated {info}')
                else:
                    # TODO: 업데이트 날짜와 이전 파일 날짜 비교해서 안된 것 업데이트
                    merge_df = apply_score(path=file_list[-1], merge_df=merge_df)
        else:
            # 스코어 값이 없기 때문에 모든 file 추가
            file_path = file_list[0]
            data = pd.read_csv(file_path)
            data['score'] = data['rank'].apply(lambda x: 21 - x)
            merge_df = data[['keyword', 'score']]
            for file_path in file_list[1:]:
                merge_df = apply_score(path=file_path, merge_df=merge_df)
            extract_update_date = file_list[-1].split('\\')[-1].split('_')[0]
    except Exception:
        print(f'error occurred! {info}')
    else:
        merge_df.to_csv(path_or_buf=f'{directory}/score.csv', index=False)
        set_update_date(directory, extract_update_date)
        print(f'finish calculated to {info}')

if __name__ == '__main__':
    # score 업데이트
    all_dir = glob.glob('data/crawling/*')
    # 디렉토리 반복
    for directory in all_dir:
        calculation_score(directory)
        # delete_file(directory)
