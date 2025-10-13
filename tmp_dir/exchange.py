import codecs


def write_text_to_file(output_filepath, content):
    """
    将文本内容以UTF-8编码写入到指定文件中。
    """
    try:
        # 步骤 3: 以写模式('w')和UTF-8编码打开输出文件，并写入解码后的内容。
        with open(output_filepath, 'a', encoding='utf-8') as f:
            f.write(content)
        print(f"成功！已将解码后的内容写入到文件: {output_filepath}")
        return True

    except Exception as e:
        print(f"写入文件时发生错误: {e}")
        return False


def read_and_decode_file(filepath):
    """
    Reads a file and correctly decodes all Unicode escape sequences,
    including surrogate pairs for emojis and special characters.
    """
    try:
        # Step 1: Read the raw bytes from the file.
        with open(filepath, 'rb') as f:
            raw_bytes = f.read()

        # Step 2: Use the 'unicode_escape' codec to interpret all \uXXXX
        # and \UXXXXXXXX sequences correctly.
        decoded_text = raw_bytes.decode('unicode_escape')
        
        return decoded_text

    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
        return None
    except Exception as e:
        print(f"An error occurred while reading or decoding the file: {e}")
        return None

# --- Main execution ---
file_path = '/root/docker/dify/dify/tmp_dir/output_filename.txt'
chinese_text = read_and_decode_file(file_path)

if chinese_text:
    # To prevent any possible printing errors, we can encode to UTF-8
    # and specify how to handle any remaining errors.
    try:
        write_text_to_file("./chinese.txt",chinese_text)
        print(chinese_text)
    except UnicodeEncodeError as e:
        print("---")
        print(f"Error printing content: {e}")
        print("Content contains invalid characters that cannot be displayed in a UTF-8 terminal.")
        print("Printing a 'safe' version of the text:")
        # This will replace invalid characters with '?' or '\ufffd'
        safe_text = chinese_text.encode('utf-8', errors='replace').decode('utf-8')
        write_text_to_file("./chinese.txt",safe_text)
        print(safe_text)
        print("---")