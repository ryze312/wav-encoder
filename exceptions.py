class WaveEncodingError(Exception):
    """Base class for wave encoding exceptions"""
    pass


class WaveDecodingError(Exception):
    """Base class for wave decoding exceptions"""
    pass


class SampleRateError(WaveEncodingError):
    """Exception for unsupported sample rate"""

    def __init__(self, sample_rate):
        self.sample_rate = sample_rate

        super().__init__(f"Sample rate must be positive: {sample_rate}")


class BitDepthError(WaveEncodingError):
    """Exception for unsupported bit depth"""

    def __init__(self, bit_depth):
        self.bit_depth = bit_depth

        super().__init__(f"Unsupported bit depth: {bit_depth}")


class BitDepthNotPositiveError(WaveEncodingError):

    def __init__(self, bit_depth):
        self.bit_depth = bit_depth

        super().__init__(f"Bit depth must be positive\n Your depth is {bit_depth}")

class ChannelsNumberError(WaveEncodingError):
    """Exception for non-positive channel number"""

    def __init__(self, channels_num):
        self.channels_num = channels_num

        super().__init__(f"Channel number must be positive\n Your number is {channels_num}")


class FileSizeError(WaveDecodingError):

    def __init__(self, file_size):
        self.file_size = file_size

        super().__init__(f"File size must be greater than 44 bytes\n Your size is {file_size}")