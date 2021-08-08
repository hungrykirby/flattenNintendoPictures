import glob
import os
import datetime
import shutil

# Nintendoという名前のフォルダを中身ごとカレントディレクトリにコピーしている前提
NINTENDO_FOLDER_NAME = 'Nintendo'
# 実行前にカレントディレクトリにOutputというフォルダを作って実行
OUTPUT = 'Output'

def mkdir_with_timestamp_in_output():
    dt_now = datetime.datetime.now()
    dirname_with_timestamp = dt_now.strftime('%Y%m%d%H%M%S')
    output_dir = os.path.join(OUTPUT, dirname_with_timestamp)
    os.mkdir(output_dir)
    return output_dir

def main():
    # テスト時にめんどくさいのでOutputというディレクトリの中に実行時間のフォルダを作成してその中にコピーする
    output_dir = mkdir_with_timestamp_in_output()
    # Nintendo / Album / #{year} / #{month} / #{date} というディレクトリ構造のはずなのでこれでフォルダがすべて取得できる
    jpg_images_path = os.path.join(NINTENDO_FOLDER_NAME, 'Album', '*', '*', '*')
    # jpg or mp4ファイルのはずだが拡張子を限定していない。
    files = glob.glob(jpg_images_path + '/*')
    for f in files:
        # 拡張子を含めたファイル名だけを取得
        # コピー後もファイル名を引き継ぎたいのでこうしている
        basename = os.path.basename(f)
        output_file = os.path.join(output_dir, basename)
        # copy2関数：ファイルのメタデータ（作成時間、変更時間、その他の情報）も可能な限りコピーしようとすることを除けばcopy関数と同様
        # メタデータもコピーしておく
        # どこまで厳密にコピーしてくれるのかは知らない
        shutil.copy2(f, output_file)

if __name__ == "__main__":
    main()