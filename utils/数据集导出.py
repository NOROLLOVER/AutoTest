from modelscope.msdatasets import MsDataset


def test():
    ds = MsDataset.load('AI-ModelScope/ruozhiba', subset_name='post-annual', split='train')
    print(next(iter(ds)))

if __name__ == '__main__':
    test()