from lib import *

def make_datapath_list(root_path):


    train_img_list = list()
    train_annotation_list = list()

    val_img_list = list()
    val_annotation_list = list()

    for file in os.listdir("./data/datafolder/train"):
        if file.endswith('.jpg'):
            train_img_list.append(os.path.join(root_path, "train", file))
        else:
            train_annotation_list.append(os.path.join(root_path, "train", file))

    
    for file in os.listdir("./data/datafolder/valid"):
        if file.endswith('.jpg'):
            val_img_list.append(os.path.join(root_path, "valid", file))
        else:
            val_annotation_list.append(os.path.join(root_path, "valid", file))

    return train_img_list, train_annotation_list, val_img_list, val_annotation_list


if __name__ == "__main__":
    root_path = "./data/datafolder/"
    train_img_list, train_annotation_list, val_img_list, val_annotation_list = make_datapath_list(root_path)

    print(len(train_img_list))
    print(train_img_list[0])
    print(train_annotation_list[0])