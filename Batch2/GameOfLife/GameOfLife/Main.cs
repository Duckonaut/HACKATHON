using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Graphics;
using Microsoft.Xna.Framework.Input;

namespace GameOfLife
{
	/// <summary>
	/// This is the main type for your game.
	/// </summary>
	public class Main : Game
	{
		private static readonly Rectangle GameStateButton = new Rectangle(0, 256, 256, 64);

		GraphicsDeviceManager graphics;
		SpriteBatch spriteBatch;

		Texture2D pixel;
		Texture2D playButton;
		Texture2D pauseButton;

		bool[,] gameBoard;
		bool inputMode;
		int playSpeed = 6;
		int updateCounter;

		MouseState previousMouseState;
		MouseState currentMouseState;

		public Main()
		{
			graphics = new GraphicsDeviceManager(this);
			graphics.PreferredBackBufferWidth = 256;
			graphics.PreferredBackBufferHeight = 320;
			Window.AllowUserResizing = false;
			IsMouseVisible = true;
			Content.RootDirectory = "Content";
		}

		protected override void Initialize()
		{
			gameBoard = new bool[16, 16];

			inputMode = true;

			base.Initialize();
		}

		protected override void LoadContent()
		{
			// Create a new SpriteBatch, which can be used to draw textures.
			spriteBatch = new SpriteBatch(GraphicsDevice);

			pixel = new Texture2D(GraphicsDevice, 1, 1);
			pixel.SetData<Color>(new Color[1] { Color.White });

			playButton = Content.Load<Texture2D>("play");
			pauseButton = Content.Load<Texture2D>("pause");
		}

		protected override void UnloadContent()
		{
			pixel.Dispose();
		}

		protected override void Update(GameTime gameTime)
		{
			currentMouseState = Mouse.GetState();

			bool mouseClick = currentMouseState.LeftButton == ButtonState.Pressed && previousMouseState.LeftButton == ButtonState.Released;

			

			if (inputMode)
			{
				if (mouseClick)
				{
					Point posOnBoard = new Point(currentMouseState.Position.X / 16, currentMouseState.Position.Y / 16);

					if (new Rectangle(0, 0, 15, 15).Contains(posOnBoard))
					{
						gameBoard[currentMouseState.Position.X / 16, currentMouseState.Position.Y / 16] = !gameBoard[currentMouseState.Position.X / 16, currentMouseState.Position.Y / 16];
					}
					else
					{
						if (GameStateButton.Contains(currentMouseState.Position))
						{
							inputMode = false;
						}

					}
				}
			}
			else
			{
				if (mouseClick && GameStateButton.Contains(currentMouseState.Position))
				{
					inputMode = true;
				}

				if (updateCounter <= 0)
				{
					bool[,] previousGameBoard = gameBoard.Clone() as bool[,];

					for (int i = 0; i < 16; i++)
					{
						for (int j = 0; j < 16; j++)
						{
							int neighborCount = 0;

							for (int x = -1; x < 2; x++)
								for (int y = -1; y < 2; y++)
									if (!(x == 0 && y == 0))
										if (previousGameBoard[(i + x + 16) % 16, (j + y + 16) % 16]) neighborCount++;

							if (previousGameBoard[i,j])
							{
								if (neighborCount < 2 || neighborCount > 3) gameBoard[i, j] = false;
							}
							else
							{
								if (neighborCount == 3) gameBoard[i, j] = true;
							}
						}
					}
					
					updateCounter = playSpeed;
				}
				else
				{
					updateCounter--;
				}
			}

			previousMouseState = currentMouseState;

			base.Update(gameTime);
		}

		protected override void Draw(GameTime gameTime)
		{
			GraphicsDevice.Clear(Color.Black);

			spriteBatch.Begin(SpriteSortMode.Immediate, BlendState.AlphaBlend, SamplerState.PointClamp);

			for (int i = 0; i < 16; i++)
			{
				for (int j = 0; j < 16; j++)
				{
					spriteBatch.Draw(pixel, new Rectangle(i * 16 + 1, j * 16 + 1, 14, 14), Color.White);
					spriteBatch.Draw(pixel, new Rectangle(i * 16 + 3, j * 16 + 3, 10, 10), Color.Black);

					if (gameBoard[i, j]) 
						spriteBatch.Draw(pixel, new Rectangle(i * 16 + 4, j * 16 + 4, 8, 8), Color.White);
				}
			}
			
			spriteBatch.Draw(inputMode ? playButton : pauseButton, GameStateButton, Color.White);


			spriteBatch.End();


			base.Draw(gameTime);
		}
	}
}
