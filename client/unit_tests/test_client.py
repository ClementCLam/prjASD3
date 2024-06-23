import unittest
import os
import shutil
import tempfile
from client.client import get_directory_info
import datetime

class TestClient(unittest.TestCase):

    def setUp(self):
        # Create a temporary directory structure for testing
        self.test_dir = tempfile.mkdtemp()
        self.file1_path = os.path.join(self.test_dir, 'file1.txt')
        self.file2_path = os.path.join(self.test_dir, 'file2.txt')
        self.subdir_path = os.path.join(self.test_dir, 'subdir')
        os.makedirs(self.subdir_path)

        # Write content to files
        with open(self.file1_path, 'w') as f:
            f.write('Content of file1')
        with open(self.file2_path, 'w') as f:
            f.write('Content of file2')
        with open(os.path.join(self.subdir_path, 'file3.txt'), 'w') as f:
            f.write('Content of file3')

        # Get modification times
        self.file1_mod_time = os.path.getmtime(self.file1_path)
        self.file2_mod_time = os.path.getmtime(self.file2_path)
        self.subdir_mod_time = os.path.getmtime(self.subdir_path)
        self.file1_mod_time_formatted = datetime.datetime.fromtimestamp(self.file1_mod_time).strftime('%Y-%m-%d %H:%M:%S')
        self.file2_mod_time_formatted = datetime.datetime.fromtimestamp(self.file2_mod_time).strftime('%Y-%m-%d %H:%M:%S')
        self.subdir_mod_time_formatted = datetime.datetime.fromtimestamp(self.subdir_mod_time).strftime('%Y-%m-%d %H:%M:%S')

    def tearDown(self):
        # Remove the temporary directory after testing
        shutil.rmtree(self.test_dir)

    def test_get_directory_info(self):
        expected_output = [
            f"file1.txt - SHA256: 76130dd839bd6067e980cc0a564d51f64fc6c3e6a5dfca59debef4bd13eb7523, Modification Time: {self.file1_mod_time_formatted}\n",
            f"file2.txt - SHA256: 172dfeec7d6d76cfa88f0e3a5a4a82ec3bb9404c7f974904ecb66bbdd9f00f0f, Modification Time: {self.file2_mod_time_formatted}\n",
            f"subdir (Dir) - 1 items, Modification Time: {self.subdir_mod_time_formatted}\n"
        ]

        # data processing to align with result
        expected_output = '\n'.join(expected_output)
        
        result = get_directory_info(self.test_dir)

        # Remove newline characters for comparison
        result_stripped = result.replace('\n', '')
        expected_output_stripped = expected_output.replace('\n', '')

        self.assertEqual(result_stripped, expected_output_stripped)

if __name__ == '__main__':
    unittest.main()