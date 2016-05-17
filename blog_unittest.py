import blog_api
import unittest


class BlogTestCase(unittest.TestCase):

    def setUp(self):
        self.app = blog_api.app.test_client()
        blog_api.app.config['TESTING'] = True

    # def tearDown(self):
    #    pass

    def test_view(self):
        print "running view test"
        ret = self.app.get("/blog/api/v1.0/view")
        print ret.data

    def test_create(self):
        print "running create test"
        data = r'{"title": "test_title", "text": "test_text", "publisher_name": "test_publishername"}'
        ret = self.app.post("/blog/api/v1.0/create", data=data, follow_redirects=True,
                            content_type = 'application/json')
        assert 'blog created successfully' in ret.data

    def test_edit(self):
        print "running edit test"
        data = r'{"title": "test_title1", "text": "test_text1", "publisher_name": "test_publishername1"}'
        ret = self.app.put("/blog/api/v1.0/blogs/1", data=data, follow_redirects=True,
                           content_type='application/json')
        assert 'blog updated successfully' in ret.data

    def test_delete(self):
        print "running delete test"
        ret = self.app.delete("/blog/api/v1.0/blogs/3")
        assert 'blog deleted successfully' in ret.data

if __name__ == '__main__':
    unittest.main()
