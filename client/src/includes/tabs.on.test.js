import Tabs from './tabs.js';

describe('Tabs Class', () => {
  let tabs;
  let tabContainer;

  beforeEach(() => {
    tabContainer = document.createElement('div');
    tabContainer.setAttribute('data-tabs', '');
    tabContainer.innerHTML = `
      <div role="tablist">
        <a href="#tab1" role="tab" aria-selected="true" aria-controls="tab1">Tab 1</a>
        <a href="#tab2" role="tab" aria-selected="false" aria-controls="tab2">Tab 2</a>
      </div>
      <div role="tabpanel" id="tab1">Content 1</div>
      <div role="tabpanel" id="tab2">Content 2</div>
    `;
    document.body.appendChild(tabContainer);
    tabs = new Tabs(tabContainer);
  });

  afterEach(() => {
    document.body.innerHTML = '';
  });

  test('case01', () => {
    window.location.hash = '#tab1';
    tabs.disableURL = false;

    const selectTabByURLHashSpy = jest.spyOn(tabs, 'selectTabByURLHash');

    tabs.onComponentLoaded();

    expect(selectTabByURLHashSpy).toHaveBeenCalled();
  });

  test('case02', () => {
    window.location.hash = '#tab1';
    tabs.disableURL = true;

    const selectTabByURLHashSpy = jest.spyOn(tabs, 'selectTabByURLHash');

    tabs.onComponentLoaded();

    expect(selectTabByURLHashSpy).not.toHaveBeenCalled();
  });

  test('case03', () => {
    window.location.hash = '';
    tabs.disableURL = false;

    const selectTabSpy = jest.spyOn(tabs, 'selectTab');

    tabs.onComponentLoaded();

    expect(selectTabSpy).toHaveBeenCalledWith(tabs.tabButtons[0]);
  });

});

