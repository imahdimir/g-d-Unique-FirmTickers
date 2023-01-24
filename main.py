"""

  """

import json
from pathlib import Path


from githubdata import GitHubDataRepo
from mirutil.ns import update_ns_module

update_ns_module()
import ns

gdu = ns.GDU()
c = ns.Col()

def main() :
    pass

    ##

    gdsa = GitHubDataRepo(gdu.srca)
    gdsa.clone_overwrite()

    ##
    df = gdsa.read_data()

    ##
    gdsb = GitHubDataRepo(gdu.srcb)
    gdsb.clone_overwrite()

    ##
    dfb = gdsb.read_data()

    ##
    dfb = dfb[[c.btic , c.ftic]]
    dfb = dfb.drop_duplicates()

    ##
    dfb = dfb.set_index(c.btic)

    ##
    df['f'] = df[c.ftic].map(dfb[c.ftic])

    ##
    msk = df['f'].notna()

    df.loc[msk , c.ftic] = df.loc[msk , 'f']
    print(len(msk[msk]))

    ##
    df = df.drop(columns = ['f'])

    ##
    df = df.drop_duplicates()
    df = df.astype('string')

    ##
    df.to_csv(gdsa.data_fp , index = False)

    ##
    msg = 'gov by: '
    msg += gdu.slf

    ##
    gdsa.commit_and_push(msg)

    ##
    gdsa.rmdir()
    gdsb.rmdir()

##


if __name__ == "__main__" :
    main()
    print(f'{Path(__file__).name} Done!')
