from optimum.onnxruntime import ORTModelForFeatureExtraction
from transformers import BertTokenizer
import pathlib





def conver_to_onnx(model_poth, onnx_save_path):
    """将 torch 模型转换为 onnx
    
    定制化的转换 china-roberta-wwm-ext-large
    """
    print('read...')
    tokenizer = BertTokenizer.from_pretrained(model_poth)
    model = ORTModelForFeatureExtraction.from_pretrained(model_poth, export=True)
    
    print('save...')
    model.save_pretrained(onnx_save_path)
    tokenizer.save_pretrained(onnx_save_path)
    
    print(f'onnx model saved to {onnx_save_path}')
    

def compare_model(model_ori_path, model_onnx_path):
    """对比两个模型的输出，推理用时。
    
    定制化对比  china-roberta-wwm-ext-large
    """ 
    
    
    
    
if __name__ == '__main__':
    model_path = pathlib.Path(r"D:\aragorn\models\chinese-roberta-wwm-ext-large")
    save_path = pathlib.Path(r"D:\aragorn\models\chinese-roberta-wwm-ext-large-onnx")
    
    # conver_to_onnx(model_path, save_path)  # convert_model
    
    