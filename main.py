import wave_helper
from os.path import getsize


def main(input_path, output_path, encoding, file_size):
    if encoding:
        print("-- Encoding ---")

        sample_rate = int( input("Enter sample rate: ") )
        bits_per_sample = int( input("Enter bit depth: ") )
        channels_num = int( input("Enter number of channels: ") )
        wave_helper.check_encoding_params(sample_rate, channels_num, bits_per_sample)

        header = wave_helper.form_header(sample_rate, channels_num, bits_per_sample, file_size)

        with open(input_path, "rb") as input_file:
            data = input_file.read()

        with open(output_path, "wb") as output_file:
            output_file.write(header)
            output_file.write(data)

    else:
        print("--- Decoding ---")

        wave_helper.check_decoding_params(file_size)

        with open(input_path, "rb") as input_file:
            input_file.seek(44)
            data = input_file.read()

        with open(output_path, "wb") as output_file:
            output_file.write(data)


input_path = input("Enter input file: ")
output_path = input("Enter output file: ")

is_encoding = input("Encoding/Decoding (E/D): ").capitalize() == "E"
file_size = getsize(input_path)

main(input_path, output_path, is_encoding, file_size)
