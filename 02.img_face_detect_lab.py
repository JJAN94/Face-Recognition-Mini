#-*- coding: utf-8 -*- 
import os
import pathlib
import glob
import cv2
import settings

def preprocessing_images_name(image_dir):
    # 이미지 이름 변경 전처리 함수
    name_ls = [[name, name[:6]+'.jpg'] for name in os.listdir(image_dir) if '.jpg' not in name]
    # 편의상 jpg 포맷으로 다 변환해줄 것임.
    # 이미지 네이밍 규칙상 idx=5까지 쓰고 뒤에 jpg로 확장자를 붙여줄 것임.
    if name_ls:
        for i,v in name_ls:
            oldname = os.path.join(image_dir, i)
            newname = os.path.join(image_dir, v)
            
            os.rename(oldname, newname)
    

# 이 함수가 왜필요한지 모르겠음
def load_name_images(image_path_pattern):
    name_images = []
    
    # 지정한 Path Pattern에 일치하는 파일 얻기
    image_paths = glob.glob(image_path_pattern)
    print(image_paths)
    # 파일별로 읽기
    for image_path in image_paths:
    #   파일 경로
        image_dir = os.path.dirname(image_path)
    #   파일명
        image_name = os.path.basename(image_path)
    #   이미지 읽기 (여기서 이미지를 왜 읽는지를 모르겠음, cv로 불러오는건지... )
        img = cv2.imread('image_path')
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        
        cv2.imshow('img', img)
        cv2.waitKey()
        cv2.destroyAllWindows()
    # return name_images

def detect_image_face(file_path, image, cascade_filepath):
    pass
    # 이미지 파일의 Grayscale화
    # 캐스케이드 파일 읽기
    # https://docs.opencv.org/3.4/db/d28/tutorial_cascade_classifier.html 참고
    # 얼굴인식
    # TO-DO 

    # 1개 이상의 얼굴인식
    # TO-DO 

def delete_dir(dir_path, is_delete_top_dir=True):
    for root, dirs, files in os.walk(dir_path, topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))
    if is_delete_top_dir:
        os.rmdir(dir_path)

RETURN_SUCCESS = 0
RETURN_FAILURE = -1
# Origin Image Pattern
IMAGE_PATH_PATTERN = "./download_imageV2/*.jpg"
# Output Directory
OUTPUT_IMAGE_DIR = "./download_face_image"

image_dir = './download_imageV2_copy'

# Cascade File Path
cascade_filepath = settings.CASCADE_FILE_PATH

def main():
    print("===================================================================")
    print("이미지 얼굴인식 OpenCV 이용")
    print("지정한 이미지 파일의 정면얼굴을 인식하고, 64x64 사이즈로 변경")
    print("===================================================================")

    # 디렉토리 작성
    if not os.path.isdir(OUTPUT_IMAGE_DIR):
        os.mkdir(OUTPUT_IMAGE_DIR)
    # 디렉토리 내의 파일 제거
    delete_dir(OUTPUT_IMAGE_DIR, False)

    
    # 이미지 파일 불러오기전 파일명 전처리 진행
    # preprocessing_images_name(image_dir)
    
    # # 이미지 파일 읽기
    load_name_images(IMAGE_PATH_PATTERN) # 여기서 name_images가 return됨
   

    # 이미지별로 얼굴인식
    # for name_image in name_images:
        
    #     # TO-DO 

    # return RETURN_SUCCESS

if __name__ == "__main__":
    IMAGE_PATH_PATTERN = "./download_imageV2/*.jpg"
    # main()
    # preprocessing_images_name('./empy')
    load_name_images(IMAGE_PATH_PATTERN)