WITH schizoposters_transfers AS (
    SELECT
        "from" AS seller,
        "to" AS buyer,
        token_id,
        block_time
    FROM nft.transfers
    WHERE contract_address = 0xbfe47d6d4090940d1c7a0066b63d23875e3e2ac5
),
buyer_stats AS (
    SELECT
        buyer,
        COUNT(*) AS tokens_bought,
        COUNT(DISTINCT token_id) AS unique_tokens_bought
    FROM schizoposters_transfers
    WHERE buyer != 0x0000000000000000000000000000000000000000  -- Exclude minting
    GROUP BY buyer
),
seller_stats AS (
    SELECT
        seller,
        COUNT(*) AS tokens_sold,
        COUNT(DISTINCT token_id) AS unique_tokens_sold
    FROM schizoposters_transfers
    WHERE seller != 0x0000000000000000000000000000000000000000  -- Exclude burning
    GROUP BY seller
)
SELECT
    COALESCE(b.buyer, s.seller) AS address,
    COALESCE(b.tokens_bought, 0) AS tokens_bought,
    COALESCE(b.unique_tokens_bought, 0) AS unique_tokens_bought,
    COALESCE(s.tokens_sold, 0) AS tokens_sold,
    COALESCE(s.unique_tokens_sold, 0) AS unique_tokens_sold,
    COALESCE(b.tokens_bought, 0) - COALESCE(s.tokens_sold, 0) AS net_tokens,
    COALESCE(b.tokens_bought, 0) + COALESCE(s.tokens_sold, 0) AS total_transactions
FROM buyer_stats b
FULL OUTER JOIN seller_stats s ON b.buyer = s.seller
ORDER BY total_transactions DESC