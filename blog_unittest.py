import blog_api
import unittest


class BlogTestCase(unittest.TestCase):

    def setUp(self):
        self.app = blog_api.app.test_client()
        blog_api.app.config['TESTING'] = True

    def tearDown(self):
        pass

    def test_view(self):
        ret = self.app.get("/blog/api/v1.0/view")
        assert 'No blogs found' in ret.data

    def test_create(self):

        data = {"title": "test_title", "text": "test_text", "publisher_name": "test_publishername"}
        ret = self.app.post("/blog/api/v1.0/create", data = data, follow_redirects=True)
        assert 'blog created successfully' in ret.content

    def test_edit(self):
        data = {"title": "test_title1", "text": "test_text1", "publisher_name": "test_publishername1"}
        ret = self.app.put("/blog/api/v1.0/blogs/1", data = data, follow_redirects=True)
        assert 'blog updated successfully' in ret.content

    def test_delete(self):
        ret = self.app.delete("/blog/api/v1.0/blogs/1")
        assert 'blog deleted successfully' in ret.content

if __name__ == '__main__':
    unittest.main()