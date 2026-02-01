import re

def extract_urls(text):
    """Get URLs from a block of text."""

    url_pattern = r'(https?://[^\s]+)'
    links = re.findall(url_pattern, text)

    yt_links = [url for url in links if ("youtube.com/watch" in url) or ("youtu.be" in url)]
    other_links = [url for url in links if url not in yt_links]
    
    return yt_links, other_links


def search_other_links(link_list):
    """Search for a YouTube video for links from other sources."""

    return []


def generate_playlist_link(link_list):
    """Convert a list of links into a YouTube temporary playlist link."""
    video_ids = []

    for url in link_list:

        if "v=" in url:
            video_ids.append(url.split("v=")[1].split("&")[0])
        elif "youtu.be/" in url:
            video_ids.append(url.split("youtu.be/")[1].split("?")[0])

    return f"https://www.youtube.com/watch_videos?video_ids={','.join(video_ids)}"


custom_css = """
<style>
.stMainBlockContainer{
    padding-top: 50px;
}

.st-emotion-cache-198znwi hr {
    margin-top: -5px;
    margin-bottom: 25px;
    }
</style>
"""

footer_css = """
<style>


.footer {
    position: fixed;
    left: 0;
    bottom: 0;
    width: 100%;
    text-align: center;
    padding: 10px 0;
    z-index: 999;
    
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 40px;
}

.footer a {
    color: rgb(153, 153, 153);
    text-decoration: none;
    display: flex;
    align-items: center;

}

.footer a:hover {
    text-decoration: underline;
    color: rgb(255, 197, 138);
}

</style>

<div class="footer">
    <a href="https://github.com/ajhenne/chat2playlist" target="_blank">GitHub</a>
    <a href="https://www.linkedin.com/in/ajhennessy/" target="_blank">LinkedIn</a>
</div>
"""
