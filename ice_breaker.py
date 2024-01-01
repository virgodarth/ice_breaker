from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain_community.document_loaders import WebBaseLoader

if __name__ == "__main__":
    # loader = WebBaseLoader("https://docs.smith.langchain.com/overview")
    # docs = '. '.join(loader.load())

    information = """
    Background

Before bitcoin, several digital cash technologies were released, starting with David Chaum's ecash in the 1980s.[12] The idea that solutions to computational puzzles could have some value was first proposed by cryptographers Cynthia Dwork and Moni Naor in 1992.[12] The concept was independently rediscovered by Adam Back who developed Hashcash, a proof-of-work scheme for spam control in 1997.[12] The first proposals for distributed digital scarcity-based cryptocurrencies came from cypherpunks Wei Dai (b-money) and Nick Szabo (bit gold) in 1998.[13] In 2004, Hal Finney developed the first currency based on reusable proof-of-work.[14] These various attempts were not successful:[12] Chaum's concept required centralized control and no banks wanted to sign on, Hashcash had no protection against double-spending, while b-money and bit gold were not resistant to Sybil attacks.[12]
2008–2009: Creation
External image
image icon Cover page of The Times 3 January 2009 showing the headline used in the genesis block
Bitcoin logos made by Satoshi Nakamoto in 2009 (left) and 2010 (right) depict bitcoins as gold tokens.

The domain name bitcoin.org was registered on 18 August 2008.[15] On 31 October 2008, a link to a white paper authored by Satoshi Nakamoto titled Bitcoin: A Peer-to-Peer Electronic Cash System was posted to a cryptography mailing list.[16] Nakamoto implemented the bitcoin software as open-source code and released it in January 2009.[8] Nakamoto's identity remains unknown.[7] All individual components of bitcoin originated in earlier academic literature.[12] Nakamoto's innovation was their complex interplay resulting in the first decentralized, Sybil resistant, Byzantine fault tolerant digital cash system, that would eventually be referred to as the first blockchain.[12][17] Nakamoto's paper was not peer-reviewed and initially ignored by academics, who argued that it could not work, based on theoretical models, even though it was working in practice.[12]

On 3 January 2009, the bitcoin network was created when Nakamoto mined the starting block of the chain, known as the genesis block.[18] Embedded in this block was the text "The Times 03/Jan/2009 Chancellor on brink of second bailout for banks", which is the date and headline of an issue of The Times newspaper.[8] Nine days later, Hal Finney received the first bitcoin transaction: ten bitcoins from Nakamoto.[19] Wei Dai and Nick Szabo were also early supporters.[18] In 2010, the first known commercial transaction using bitcoin occurred when programmer Laszlo Hanyecz bought two Papa John's pizzas for ₿10,000.[20]
2010–2012: Early growth

Blockchain analysts estimate that Nakamoto had mined about one million bitcoins[21] before disappearing in 2010 when he handed the network alert key and control of the code repository over to Gavin Andresen. Andresen later became lead developer at the Bitcoin Foundation,[22][23] an organization founded in September 2012 to promote bitcoin.[24]

After early "proof-of-concept" transactions, the first major users of bitcoin were black markets, such as the dark web Silk Road. During its 30 months of existence, beginning in February 2011, Silk Road exclusively accepted bitcoins as payment, transacting ₿9.9 million, worth about $214 million.[25]: 222 
2013–2014: First regulatory actions

In March 2013, the US Financial Crimes Enforcement Network (FinCEN) established regulatory guidelines for "decentralized virtual currencies" such as bitcoin, classifying American bitcoin miners who sell their generated bitcoins as money services businesses, subject to registration and other legal obligations.[26] In May 2013, US authorities seized the unregistered exchange Mt. Gox.[27] In June 2013, the US Drug Enforcement Administration seized ₿11.02 from a man attempting to use them to buy illegal substances. This marked the first time a government agency had seized bitcoins.[28] The FBI seized about ₿30,000 in October 2013 from Silk Road, following the arrest of its founder Ross Ulbricht.[29]

In December 2013, the People's Bank of China prohibited Chinese financial institutions from using bitcoin.[30] After the announcement, the value of bitcoin dropped,[31] and Baidu no longer accepted bitcoins for certain services.[32] Buying real-world goods with any virtual currency had been illegal in China since at least 2009.[33]
2015–2019

Research produced by the University of Cambridge estimated that in 2017, there were 2.9 to 5.8 million unique users using a cryptocurrency wallet, most of them using bitcoin.[34] In August 2017, the SegWit software upgrade was activated. Segwit was intended to support the Lightning Network as well as improve scalability.[35] SegWit opponents, who supported larger blocks as a scalability solution, forked to create Bitcoin Cash, one of many forks of bitcoin.[36]

In February 2018, price crashed after China imposed a complete ban on Bitcoin trading.[37] The percentage of bitcoin trading in the Chinese renminbi fell from over 90% in September 2017 to less than 1% in June 2018.[38] During the same year, Bitcoin prices were negatively affected by several hacks or thefts from cryptocurrency exchanges.[39]
2020–present
Bitcoin price in US dollars

In 2020, some major companies and institutions started to acquire bitcoin: MicroStrategy invested $250 million in bitcoin as a treasury reserve asset,[40] Square, Inc., $50 million,[41] and MassMutual, $100 million.[42] In November 2020, PayPal added support for bitcoin in the US.[43]

In February 2021, Bitcoin's market capitalization reached $1 trillion for the first time.[44] In November 2021, the Taproot soft-fork upgrade was activated, adding support for Schnorr signatures, improved functionality of smart contracts and Lightning Network.[45] Before, Bitcoin only used a custom elliptic curve with the ECDSA algorithm to produce signatures.[46]: 101  In September 2021, Bitcoin became legal tender in El Salvador, alongside the US dollar.[4]

In May and June 2022, the bitcoin price fell following the collapses of TerraUSD, a stablecoin,[47] and the Celsius Network, a decentralized finance loan company.[48][49]

In 2023, ordinals, non-fungible tokens (NFTs) on Bitcoin, went live.[50] 
"""

    summary_template = """
        give the information {information} about a crypto currency from I want you create:
        1. a short summary of the whole
        2. two interesting facts about them
    """

    summary_template_prompt = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm = ChatOpenAI(
        model_name="gpt-3.5-turbo"
    )

    chain = LLMChain(
        llm=llm,
        prompt=summary_template_prompt
    )

    print(chain.run(information=information))
