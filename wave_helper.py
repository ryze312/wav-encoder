import exceptions
from struct import pack


def check_encoding_params(sample_rate, channels_num, sample_bits):
    if sample_rate <= 0:
        raise exceptions.SampleRateError(sample_rate)

    elif sample_bits > 32:
        raise exceptions.BitDepthError(sample_bits)

    elif sample_bits <= 0:
        raise exceptions.BitDepthNotPositiveError(sample_bits)

    elif channels_num <= 0:
        raise exceptions.SampleRateError(channels_num)


def check_decoding_params(file_size):
    if file_size < 44:
        raise exceptions.FileSizeError(file_size)


def form_header(sample_rate, channels_num, sample_bits, file_size):
    header = bytearray()

    riff = "RIFF".encode("ascii")
    wave = "WAVE".encode("ascii")
    fmt = "fmt ".encode("ascii")
    data = "data".encode("ascii")
    chunk_size = file_size + 36

    byte_rate = sample_rate * channels_num * sample_bits // 8  # SampleRate * NumChannels * BitsPerSample / 8
    block_align = channels_num * sample_bits // 8              # NumChannels * BitsPerSample / 8

    header.extend( pack(">4s", riff) )             # RIFF
    header.extend( pack("<I", chunk_size) )        # Chunk size (file size + 36)
    header.extend( pack(">4s", wave) )             # WAVE Format
    header.extend( pack(">4s", fmt) )              # Format chunk
    header.extend( pack("<I", 16) )                # Format chunk size
    header.extend( pack("<H", 1) )                 # PCM AudioFormat
    header.extend( pack("<H", channels_num) )      # Number of channels
    header.extend( pack("<I", sample_rate) )       # Sample Rate
    header.extend( pack("<I", byte_rate) )         # Byte rate
    header.extend( pack("<H", block_align) )       # Block Align
    header.extend( pack("<H", sample_bits) )       # Bits/sample
    header.extend( pack(">4s", data) )             # Data Chunk
    header.extend( pack("<I", file_size) )         # Data chunk size

    return header