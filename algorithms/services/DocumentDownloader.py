import re
import os
import requests


class DocumentDownloader:

    def extract_file_id(self, url):
        """Extract the Google file ID from a Docs/Slides/Drive URL."""
        match = re.search(r'/d/([a-zA-Z0-9_-]+)', url)
        if not match:
            match = re.search(r'id=([a-zA-Z0-9_-]+)', url)
        return match.group(1) if match else None


    def download_google_drive_file(self, url, output_dir):
        # Extract the file ID from the URL
        file_id = file_id = self.extract_file_id(url)

        # Construct the direct download URL
        download_url = f"https://drive.google.com/uc?export=download&id={file_id}"

        # Make the request
        response = requests.get(download_url, stream=True)
        if response.status_code != 200:
            raise
            return None

        # Extract filename from the response headers
        content_disposition = response.headers.get('Content-Disposition', '')
        filename_match = re.search(r'filename="(.+)"', content_disposition)
        filename = filename_match.group(1) if filename_match else "downloaded_file"

        # Ensure the output directory exists
        os.makedirs(output_dir, exist_ok=True)
        output_path = os.path.join(output_dir, filename)

        # Write the content to a file
        with open(output_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)

        print(f"File successfully downloaded to: {output_path}")
        return output_path

    def download_google_doc_file(self, url, output_dir):
        file_id = self.extract_file_id(url)
        if not file_id:
            print("Could not extract file ID from the URL.")
            return

        export_url = f"https://docs.google.com/document/d/{file_id}/export?format=docx"
        response = requests.get(export_url)

        output_filename = ""
        if response.status_code == 200:
            os.makedirs(output_dir, exist_ok=True)
            output_filename = os.path.join(output_dir, f"{file_id}.docx")
            with open(output_filename, "wb") as f:
                f.write(response.content)
            print(f"File successfully downloaded to: {output_filename}")
        else:
            print(f"Failed to download. Status code: {response.status_code}")
        
        return output_filename

    def download_google_slides_file(self, url, output_dir):
        file_id = self.extract_file_id(url)
        if not file_id:
            print("Could not extract file ID from the URL.")
            return

        export_url = f"https://docs.google.com/presentation/d/{file_id}/export/pptx"
        response = requests.get(export_url)

        output_filename = ""
        if response.status_code == 200:
            os.makedirs(output_dir, exist_ok=True)
            output_filename = os.path.join(output_dir, f"{file_id}.pptx")
            with open(output_filename, "wb") as f:
                f.write(response.content)
            print(f"File successfully downloaded to: {output_filename}")
        else:
            print(f"Failed to download. Status code: {response.status_code}")

        return output_filename

