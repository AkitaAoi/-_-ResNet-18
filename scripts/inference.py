import torch
import torchvision.transforms as transforms
from PIL import Image
from model import net   # 导入模型结构

def main(image_path):
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    # 加载权重
    net.load_state_dict(torch.load('best_cat_dog_model.pth', map_location=device))
    net.to(device)
    net.eval()

    # 预处理（必须与训练时的验证集预处理一致）
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])

    # 加载并预处理图像
    img = Image.open(image_path).convert('RGB')
    input_tensor = transform(img).unsqueeze(0).to(device)

    # 推理
    with torch.no_grad():
        output = net(input_tensor)
        _, pred_idx = torch.max(output, 1)
        # 类别顺序请根据训练时的文件夹顺序确认，假设 0=cat, 1=dog
        class_names = ['cat', 'dog']
        predicted = class_names[pred_idx.item()]

    print(f"Prediction for {image_path}: {predicted}")
    # 可选：显示图片
    img.show()

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 2:
        print("Usage: python inference.py <image_path>")
        sys.exit(1)
    main(sys.argv[1])
