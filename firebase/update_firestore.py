import pandas as pd
import glob
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
# # 경덕
# cred = credentials.Certificate('../data/info/atte2gd-eb088-firebase-adminsdk-bftoy-36320b017e.json')
# cred = credentials.Certificate('data/info/atte2gd-eb088-firebase-adminsdk-bftoy-36320b017e.json')

# # 재희
# cred = credentials.Certificate('../data/info/atte2jh-firebase-adminsdk-27fq5-24afbf0bb4.json')
# cred = credentials.Certificate('data/info/atte2jh-firebase-adminsdk-27fq5-24afbf0bb4.json')
# firebase_admin.initialize_app(cred)
# db = firestore.client()

if __name__ == '__main__':
    if __package__ is None:
        import sys
        from os import path
        print(path.dirname(path.dirname(path.abspath(__file__))))
        sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
        from extract.helper import get_date
    else:
        from ..extract.helper import get_date
    # cred_list = ['data/info/atte2gd-eb088-firebase-adminsdk-bftoy-36320b017e.json', 'data/info/atte2jh-firebase-adminsdk-27fq5-24afbf0bb4.json']
    cred_list = ['data/info/atte2jh-firebase-adminsdk-27fq5-24afbf0bb4.json']
    for cred_path in cred_list:
        cred = credentials.Certificate(f'{cred_path}')
        firebase_admin.initialize_app(cred)
        db = firestore.client()
        all_dir = glob.glob('data/crawling/*')
        date = get_date(day='today')
        for dir_path in all_dir:
            info = dir_path.split('\\')[-1]
            age, gender, cat_id, cat_name = info.split('_')
            app_info_path = dir_path + '/today_best.csv'
            # product_path = dir_path + '/today_best_prodct.csv'
            app_info_df = pd.read_csv(app_info_path, index_col=0)
            # product_info = pd.read_csv(product_path, index_col=0).fillna('')
            app_info = app_info_df[['rank', 'keyword', 'score', 'lowPrice', 'highPrice', 'meanPrice', 'webUrl', 'imageUrl']].to_dict(orient='records')
            # all_info = app_info_df['productInfo'].to_dict()
            # app_info_df[['productInfo']]
            for i, app_data in enumerate(app_info):
                db.collection(f'{gender}').document(f'{age}').collection(f'{cat_id}').document(f'{date}').\
                    collection(f'{i+1}').document('appInfo').set(app_data)
                print(f'update successfully {gender}_{age}_{cat_name}_{date}_{i+1}')
            # # TODO product_info 추가
            # for index, row in app_info_df.iterrows():
            #     a = row['productInfo'].to_dict()
            #     db.collection(f'{gender}').document(f'{age}').collection(f'{cat_id}').document(f'{date}').\
            #         collection(f'{index+1}').document('appInfo').set(app_data)
